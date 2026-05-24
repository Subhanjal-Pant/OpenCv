import cv2 as cv
import os
import matplotlib.pyplot as plt

def readAndWriteSinglePixel():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'image.png' )
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    for i in range(60):
        requiredPixel = imgRGB[313,350]
        imgRGB[313 + i, 350 +i] = (255, 0, 0)
    # debug = 1
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

def readAndWritePixelRegion():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, "images", "image.png")
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    region = imgRGB[290:340, 326:380]
    dx = 340 - 290
    dy = 380 - 326
    startX = 238
    startY = 411
    imgRGB[startX:startX + dx, startY:startY + dy] = region
    plt.show()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == '__main__':
    # readAndWriteSinglePixel()
    readAndWritePixelRegion()
 