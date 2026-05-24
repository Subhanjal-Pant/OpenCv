import numpy as np
import matplotlib.pyplot as plt
import os 
import cv2 as cv

def convolution2d():
    n=100
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'image.png')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    kernel = np.ones((n,n), dtype=float)/(n*n)
    imgFiltered = cv.filter2D(imgRGB, -1, kernel)

    plt.figure()
    plt.subplot(121)
    plt.imshow(imgRGB)
    plt.subplot(122)
    plt.imshow(imgFiltered)
    plt.show()

if __name__ == '__main__':
    convolution2d()