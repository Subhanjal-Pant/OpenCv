import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def greyScale():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'image.png')
    img = cv.imread(imgPath)
    imgGray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('gray', imgGray)
    cv.waitKey(0)

def readAsGray():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'image.png')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    cv.imshow('gray', img)
    cv.waitKey(0)



if __name__ == "__main__":
    # greyScale()
    readAsGray()