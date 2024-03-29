import numpy as np
import cv2
import pytest

# Import functions from the provided code
from naloga2 import konvolucija, filtriraj_z_gaussovim_jedrom, filtriraj_sobel_smer, zmanjsaj_sliko

def test_konvolucija():
    image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])

    result = konvolucija(image, kernel)

    assert result.shape == image.shape # preverim ce je shape ostav enak
    assert result.dtype == np.uint8 # preverim ce je tip ostav enak

def test_filtriraj_z_gaussovim_jedrom():
    image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    sigma = 3.0

    result = filtriraj_z_gaussovim_jedrom(image, sigma)

    assert result.shape == image.shape
    assert result.dtype == np.uint8

def test_filtriraj_sobel_smer():
    horizontal_gradient = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    vertical_gradient = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)

    result = filtriraj_sobel_smer(image, horizontal_gradient, vertical_gradient)

    assert result.shape == image.shape
    assert result.dtype == np.uint8

def test_zmanjsaj_sliko():
    image = np.random.randint(0, 255, (200, 200, 3), dtype=np.uint8)

    resized_image = zmanjsaj_sliko(image, 100, 100)

    assert resized_image.shape == (100, 100, 3)
    assert resized_image.dtype == np.uint8

if __name__ == "__main__":
    pytest.main([__file__])
