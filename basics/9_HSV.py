import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np



def hsvColorSegmentation():
    pwd=os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'image.png')
    img = cv.imread(imgPath)

    if img is None:
        print("No image found")
        exit()

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lowerBound = np.array([0,0,50])
    upperBound = np.array([10,120,100])
    mask =  cv.inRange(hsv,lowerBound, upperBound)
    plt.figure()

    plt.imshow(imgRGB)
    plt.show()
    cv.imshow('masky', mask)
    
    # plt.subplot(121)
    # plt.imshow(imgRGB)
    # plt.title('RGB channel')

    # plt.subplot(122)
    # plt.imshow(hsv)
    # plt.title('HSV')
    # plt.show()
    cv.waitKey(0)

if __name__ == '__main__':
    hsvColorSegmentation()