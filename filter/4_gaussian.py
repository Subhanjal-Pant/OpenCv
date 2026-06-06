import numpy as np 
import matplotlib.pyplot as plt
import cv2 as cv
import imghdr
import os

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

def viewImage(img):
    cv.imshow("Image is: ", img)
    cv.waitKey(0)

def gaussianFiltering(img):
    print("Working on this")


if __name__ == "__main__":
    user_input = input("Enter 1 to view the image, 2 to apply Gaussian filter to the image :")
    img = get_valid_image()

    if img is not None:
        if user_input == "1":
            viewImage(img)
        elif user_input=="2":
            gaussianFiltering(img)
        else:
            print("Invalid choice")
        