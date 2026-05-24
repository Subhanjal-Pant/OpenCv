import cv2 as cv
import os


def writeVideo():
    capture = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*"XVID")
    pwd = os.getcwd()

    writePath = os.path.join(pwd, "Videos", "webcam.avi")
    out = cv.VideoWriter(writePath, fourcc, 20.0, (640,480))
    while capture.isOpened():
        ret, frame = capture.read()
        if ret:
            out.write(frame)
            cv.imshow('Webcam', frame)
        if cv.waitKey(1) == ord('q'):
            break
    capture.release()
    out.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    writeVideo()