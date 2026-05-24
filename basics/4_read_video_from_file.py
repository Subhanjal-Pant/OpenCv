import os 
import cv2 as cv
import numpy as np


def videoFromFile():
    print("Hello")
    pwd = os.getcwd()
    vidPath=os.path.join(pwd,'Videos', 'video.mp4')
    cap= cv.VideoCapture(vidPath)
    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('video', frame)
        delay = int(1000/60)
        if cv.waitKey(delay) == ord('q'):
            break




if __name__=='__main__':
    videoFromFile()