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
    bImgBlack = cv.merge((zeros, zeros, zeros))
    bImgWhite = cv.merge((ones*255, ones*255, ones*255))
    
    plt.subplot(231)
    plt.imshow(bImgRed)
    plt.title('red')

    plt.subplot(232)
    plt.imshow(bImgGreen)
    plt.title('Green')

    plt.subplot(233)
    plt.imshow(bImgBlue)
    plt.title('blue')

    plt.subplot(234)
    plt.imshow(bImgBlack)
    plt.title('blue')

    plt.subplot(235)
    plt.imshow(bImgWhite)
    plt.title('blue')


    plt.show()

def breakColorChannels():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd,'images', 'image.png')
    img = cv.imread(imgPath)
    b,g,r = cv.split(img)
    zeros = np.zeros_like(b)
    bImg = cv.merge((b, zeros, zeros))
    gImg = cv.merge((zeros, g, zeros))
    rImg = cv.merge((zeros, zeros, r))

    plt.figure()

    plt.subplot(131)
    plt.imshow(bImg)
    plt.title('Blue Channel')

    plt.subplot(132)
    plt.imshow(gImg)
    plt.title('Green Channel')

    plt.subplot(133)
    plt.imshow(rImg)
    plt.title('Red Channel')

    plt.show()



if __name__ == "__main__":
    # pureColors()
    breakColorChannels()