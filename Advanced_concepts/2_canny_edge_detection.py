# More reliable Edge detection
import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def callBack(inp):
    pass

def cannyEdge():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'tesla.png')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)

    winName = "Canny Edge Detection"
    cv.namedWindow(winName)
    cv.createTrackbar('minThres', winName, 0, 255, callBack)
    cv.createTrackbar('maxThres', winName, 0, 255, callBack)

    while True:
        if cv.waitKey(1) == ord('q'):
            break

        minThres = cv.getTrackbarPos('minThres', winName)
        maxThres = cv.getTrackbarPos('maxThres', winName)
        cannyEdge = cv.Canny(img, minThres, maxThres)
        cv.imshow(winName, cannyEdge)
    cv.destroyAllWindows()

if __name__ == "__main__":
    cannyEdge()