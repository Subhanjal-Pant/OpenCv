import os 
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def pureColors():
    zeros = np.zeros((100,100))
    ones = np.ones((100,100))

    bImgRed = cv.merge((ones*255, zeros, zeros))

    bImgGreen = cv.merge((zeros, 255*ones, zeros))

    bImgBlue = cv.merge((zeros, zeros, 255*ones))
    plt.figure()
    
    
    plt.subplot(231)
    plt.imshow(bImgRed)
    plt.title('red')

    plt.subplot(232)
    plt.imshow(bImgGreen)
    plt.title('Green')
    
    plt.subplot(233)
    plt.imshow(bImgBlue)
    plt.title('blue')

    plt.show()



if __name__ == "__main__":
    pureColors()