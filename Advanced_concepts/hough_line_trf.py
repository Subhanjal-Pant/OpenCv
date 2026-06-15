import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np


def houghLineTransform():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'tesla_hough.png')
    img = cv.imread(imgPath)
    imgBlurred = cv.GaussianBlur(img, (21,21), 3)
    cannyEdge = cv.Canny(imgBlurred, 50, 180)
    plt.figure()
    plt.subplot(141)
    plt.imshow(img)
    plt.subplot(142)
    plt.imshow(imgBlurred)
    plt.subplot(143)
    plt.imshow(cannyEdge)
    plt.show()



if __name__ == "__main__":
    houghLineTransform()