# Detecting edges
import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np



def imgGradient():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'tesla.png')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)


    plt.figure()
    plt.subplot(221)
    plt.imshow(img, cmap='gray')
    laplacian = cv.Laplacian(img, cv.CV_64F, ksize=21)
    plt.subplot(222)
    plt.imshow(laplacian, cmap='gray')

    kx, ky = cv.getDerivKernels(1,0, 3)
    print(ky@kx.T)
    # cv.Sobel(img, ddepth, dx, dy, ksize)
    sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=21)
    plt.subplot(223)
    plt.imshow(sobelX, cmap='gray')

    kx, ky = cv.getDerivKernels(0, 1, 3)
    print(ky@kx.T)
    sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=21)
    plt.subplot(224)
    plt.imshow(sobelY, cmap='gray')

    plt.show()


if __name__ == "__main__":
    imgGradient()