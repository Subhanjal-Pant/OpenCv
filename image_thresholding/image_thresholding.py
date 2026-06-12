import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def imageThreshold():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'tesla.png')
    img = cv.imread(imgPath)
    plt.imshow(img)
    plt.show()


if __name__=="__main__":
    imageThreshold()