# Doesn't work well Come back when openCV is completely learnt
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2 as cv



def medianFiltering():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'tesla.png')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    noisyImg = imgRGB.copy()
    noiseProb = 0.05
    noise = np.random.rand(noisyImg.shape[0], noisyImg.shape[1])
    imgFiltered = cv.medianBlur(imgRGB,5)
    plt.figure()
    plt.imshow(imgFiltered)
    plt.show()

if __name__ == '__main__':
    medianFiltering()