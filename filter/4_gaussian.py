import numpy as np 
import matplotlib.pyplot as plt
import cv2 as cv
import imghdr
import os

def callBack(input):
    pass

def get_valid_image():
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'images', 'image.png')

    image_type = None

    if os.path.isfile(imgPath):
        image_type = imghdr.what(imgPath)
    
    if image_type is None:
        print("Image doesn't exist")
        return None
    
    return cv.imread(imgPath)

def gaussianKernel(size, sigma):
    kernel = cv.getGaussianKernel(size, sigma)
    kernel = np.outer(kernel, kernel)
    return kernel


def viewImage(img):
    cv.imshow("Image is: ", img)
    cv.waitKey(0)

def visualizeKernel(img,n):
    fig = plt.figure()
    plt.subplot(121)
    kernel = gaussianKernel(n,8)
    plt.imshow(kernel)
    ax = fig.add_subplot(122, projection='3d')
    x = np.arange(0,n,1)
    y = np.arange(0,n,1)
    X,Y = np.meshgrid(x,y)
    Z = kernel.flatten()
    ax.plot_surface(X,Y,kernel, cmap='viridis')
    plt.show()

def gaussianFiltering(img,n):
    print("Working on this")
    winName = 'Gauss Filter'
    cv.namedWindow(winName)
    cv.createTrackbar('sigma', winName, 1, 20, callBack)

    
    while True:
        if cv.waitKey(1) == ord('q'):
            break
        
        sigma = cv.getTrackbarPos('sigma', winName)
        if sigma <= 0:
            sigma = 1
        imgFilter = cv.GaussianBlur(img, (n,n), sigma)
        cv.imshow(winName, imgFilter)

    cv.destroyAllWindows()

if __name__ == "__main__":
    user_input = input("Enter 1 to view the image, 2 to apply Gaussian filter to the image and 3 to visualize the kernel :")
    img = get_valid_image()
    n=51

    if img is not None:
        if user_input == "1":
            viewImage(img)
        elif user_input=="2":
            gaussianFiltering(img,n)
        elif user_input=="3":
            visualizeKernel(img,n)
        else:
            print("Invalid choice")
        