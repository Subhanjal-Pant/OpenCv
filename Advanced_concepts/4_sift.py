import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def sift():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'tesla.png')
    imgGray = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    
    sift = cv.SIFT_create()
    keypoints = sift.detect(imgGray, None)
    imgGray = cv.drawKeypoints(imgGray, keypoints, imgGray, flags = cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    plt.figure()
    plt.imshow(imgGray)
    plt.show()
    


if __name__ == "__main__":
    sift()