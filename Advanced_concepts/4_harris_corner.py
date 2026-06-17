import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def harrisCorner():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'Images', 'logo.png')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgGray = np.float32(imgGray)
    
    plt.figure()

    plt.subplot(131)
    plt.imshow(img)

    plt.subplot(132)
    plt.imshow(imgGray)

    blockSize = 5
    sobelSize = 3
    k=0.05

    harris = cv.cornerHarris(imgGray, blockSize, sobelSize, k)

    plt.subplot(133)
    plt.imshow(harris)

    plt.show()


if __name__ == "__main__":
    harrisCorner()