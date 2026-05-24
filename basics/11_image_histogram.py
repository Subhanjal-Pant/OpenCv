import cv2 as cv
import matplotlib.pyplot as plt
import os 
import numpy as np


def Histogram():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'image.png')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    
    plt.figure()
    plt.imshow(img, cmap='gray')

    hist = cv.calcHist([img], [0], None, [256],[0,256] )
    plt.figure()
    plt.plot(hist)
    plt.xlabel('bins')
    plt.ylabel('# of pixels')
    plt.show()

def ColorHistogram():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'image.png')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    colors = ['b', 'g', 'r']
    plt.figure()
    # plt.imshow(imgRGB)
    for i in range(len(colors)):
        hist = cv.calcHist([imgRGB], [i], None, [256],[0,256])
        plt.plot(hist, color=colors[i])
        
    plt.xlabel('Pixel intensity')
    plt.ylabel('# of pixels')


    plt.show()

def regionColorHistogram():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'image.png')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgRGB = imgRGB[200:300, 200:300,:]
    colors = ['b', 'g', 'r']
    plt.figure(1)
    plt.imshow(imgRGB)
    plt.show()
    plt.figure(2)
    for i in range(len(colors)):
        hist = cv.calcHist([imgRGB], [i], None, [256],[0,256])
        plt.plot(hist, color=colors[i])
        
    plt.xlabel('Pixel intensity')
    plt.ylabel('# of pixels')


    plt.show()

if __name__ == '__main__':
    # Histogram()
    # ColorHistogram()
    regionColorHistogram()