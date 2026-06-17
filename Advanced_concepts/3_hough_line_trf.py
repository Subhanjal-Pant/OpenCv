import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np


def houghLineTransform():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'tesla_hough.png')
    img = cv.imread(imgPath)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgBlurred = cv.GaussianBlur(img, (9,9), 3)
    cannyEdge = cv.Canny(imgBlurred, 50, 180)
   
    plt.figure()
    plt.subplot(141)
    plt.imshow(img)
    plt.subplot(142)
    plt.imshow(imgBlurred)
    plt.subplot(143)
    plt.imshow(cannyEdge)

    distResol = 1
    angleResol = np.pi/180
    threshold = 150
    lines = cv.HoughLines(cannyEdge, distResol, angleResol, threshold)
    # print(lines)
    # Hough Lines return the lines 
    # Say the image has 3 lines
    # it returns rho and theta for each line
    # print(lines[0])
    k = 3000
    print(f"The number of lines is: {len(lines)}")
    if lines is not None:
        
        for curline in lines:
            rho, theta = curline[0]
            print("This is curline[0]")
            print(curline[0])
            d_hat = np.array([[np.cos(theta)], [np.sin(theta)]])
            print(d_hat)
            d = rho*d_hat
            l_hat = np.array([[-np.sin(theta)], [np.cos(theta)]])
            p1 = d + k*l_hat
            p2 = d - k*l_hat
            p1 = p1.astype(int)
            p2 = p2.astype(int)
            cv.line(img, (p1[0][0], p1[1][0]), (p2[0][0], p2[1][0]), (255,255,255), 10)
    elif lines is None:
        print("No Edges Found")
    plt.subplot(144)
    plt.imshow(img)
    plt.show()



if __name__ == "__main__":
    houghLineTransform()