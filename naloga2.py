import cv2 as cv
import numpy as np
import math
import time
import numba
from numba import jit

@jit(nopython=True)
def konvolucija(slika, jedro):
    '''Izvede konvolucijo nad sliko. Brez uporabe funkcije cv.filter2D, ali katerekoli druge funkcije, ki izvaja konvolucijo.
    Funkcijo implementirajte sami z uporabo zank oz. vektorskega računanja.'''
    visina, sirina, barvni_kanali = slika.shape
    j_h, j_w = jedro.shape
    padding = j_w // 2
    
    rezultat = np.zeros_like(slika)
    
    slika_pad = np.zeros((visina + 2 * padding, sirina + 2 * padding, barvni_kanali), dtype=slika.dtype)
    slika_pad[padding:visina + padding, padding:sirina + padding, :] = slika
    
    for c in range(barvni_kanali):
        for y in range(visina):
            for x in range(sirina):
                rezultat[y, x, c] = np.sum(slika_pad[y:y+j_h, x:x+j_w, c] * jedro)
            
    return rezultat

def filtriraj_z_gaussovim_jedrom(slika,sigma):
    '''Filtrira sliko z Gaussovim jedrom..'''
    velikost_jedra = int(2 * sigma * 2 + 1)
    jedro = np.zeros((velikost_jedra, velikost_jedra), dtype=np.float32)
    sredina = velikost_jedra // 2
    
    for i in range(velikost_jedra):
        for j in range(velikost_jedra):
            jedro[i, j] = 1 / (2 * math.pi * sigma ** 2) * math.exp(-((i - sredina -1) ** 2 + (j - sredina - 1) ** 2) / (2 * sigma ** 2))
            
    jedro /= np.sum(jedro)
    
    rezultat = konvolucija(slika.astype(np.float32), jedro)
    
    return rezultat.astype(np.uint8)

def filtriraj_sobel_smer(slika):
    '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''
    pass

def zmanjsaj_sliko(slika, sirina, visina):
    return cv.resize(slika, (sirina, visina))

if __name__ == '__main__':    
    #Pripravi kamero
    kamera = cv.VideoCapture(0)
    # Preverimo, če je kamera pravilno naložena
    if not kamera.isOpened():
        print('Kamera ni bila odprta.')
    else:
        start_time = time.time()
        fps_counter = 0
        while True:
            # Preberemo sliko iz kamere
            ret, slika = kamera.read()
            slika = cv.flip(slika, 1)
            slika = zmanjsaj_sliko(slika, 220, 340)

            key = cv.waitKey(1) & 0xFF
            # Če pritisnemo tipko 'q', zapremo okno
            if key == ord('q'):
                break

            sigma = 3
            filtrirana_slika = filtriraj_z_gaussovim_jedrom(slika, sigma)
            fps_counter += 1
            fps = fps_counter / (time.time() - start_time)
            cv.putText(filtrirana_slika ,str(int(fps)), (25, 25), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
            cv.imshow('Filtrirana slika z Gaussovim jedrom', filtrirana_slika)

        cv.destroyAllWindows()
