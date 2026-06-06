import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os

def callback(val):
    pass

def averageFiltering():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'image.png')
    img = cv.imread(imgPath)
    winName='Average Filter'
    cv.namedWindow(winname=winName)
    cv.createTrackbar('n', winName, 1, 100, callback)

    height, width, _ = img.shape
   
    # plt.figure()
    # plt.imshow(img)
    # plt.show()

    while True:
        if cv.waitKey(1)==ord('q'):
            break
        n=cv.getTrackbarPos('n', winname=winName)
        if n>=1:
            imgFilter = cv.blur(img,(n,n))
        else:
            imgFilter=img.copy()
        cv.imshow(winName, imgFilter)
    cv.destroyAllWindows()

if __name__ == '__main__':
    averageFiltering()