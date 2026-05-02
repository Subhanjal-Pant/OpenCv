import cv2 as cv
import os 
import matplotlib.pyplot as plt
import numpy as np


def readImage():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, "images", 'image.png')
    print(imgPath)
    img = cv.imread(imgPath)
    cv.imshow('hello', img)
    cv.waitKey(0)


def writeImage():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, "images", 'image.png')
    print(imgPath)
    img = cv.imread(imgPath)
    outPath = os.path.join(pwd, "images", 'outimage.png')

    cv.imwrite(outPath, img)    


if __name__ == '__main__':
    # readImage()
    writeImage()