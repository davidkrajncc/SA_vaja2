import numpy as np
import cv2
import pytest

from naloga2 import konvolucija, filtriraj_z_gaussovim_jedrom, filtriraj_sobel_smer

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

if __name__ == "__main__":
    pytest.main([__file__])
