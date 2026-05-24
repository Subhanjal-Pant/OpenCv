import numpy as np
import cv2 as cv
import os 

def videoFromWebCam():
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Camera couldn't be accessed!")
        exit()
    
    while True:
        ret, frame = capture.read()
        if ret:
            cv.imshow('WebCam', frame)
        if cv.waitKey(1) == ord('q'):
            break
    capture.release()
    cv.destroyAllWindows() 



if __name__=='__main__':
    videoFromWebCam()