import cv2 as cv
import os
import numpy as np

def lucasKanade():
    pwd = os.getcwd()
    videoPath = os.path.join(pwd, "Videos", "video.mp4")
    video = cv.VideoCapture(videoPath)
    
    shiTomasiCornerParams = dict(maxCorners=20, qualityLevel=0.3, minDistance=50, blockSize=7)

    lucasKanadeParams = dict(winSize=(25,15), maxLevel=2,criteria=(cv.TERM_CRITERIA_EPS|cv.TERM_CRITERIA_COUNT,10,0.03))

    randomColors = np.random.randint(0,255, (100,3))

    _,frameFirst = video.read()
    frameGrayPrev = cv.cvtColor(frameFirst, cv.COLOR_BGR2GRAY)
    cornersPrev = cv.goodFeaturesToTrack(frameGrayPrev,mask=None, **shiTomasiCornerParams)
    mask = np.zeros_like(frameFirst)


    if not video.isOpened():
        print(f"Error: Could not open video at {videoPath}")
        return

    while True:
        ret, frame = video.read()
        frameGrayCur = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cornersCur, foundStatus,_ = cv.calcOpticalFlowPyrLK(frameGrayPrev, frameGrayCur, cornersPrev, None, **lucasKanadeParams)
        
        if cornersCur is not None:
            cornersMatchedCur = cornersCur[foundStatus==1]
            cornerMatchedPrev = cornersPrev[foundStatus==1]

        for i,(curCorner, prevCorner) in enumerate(zip(cornersMatchedCur, cornerMatchedPrev)):
            xCur, yCur = curCorner.ravel()
            xPrev, yPrev = prevCorner.ravel()
            mask = cv.line(mask, (int(xCur), int(yCur)), (int (xPrev), int (yPrev)), randomColors[i].tolist(),2)

            frame = cv.circle(frame, (int(xCur), int (yCur)), 5, randomColors[i].tolist(),-1)

            img = cv.add(frame,mask)

      
            
        cv.imshow("Video", img)
        cv.waitKey(15)
        frameGrayPrev = frameGrayCur.copy()
        cornersPrev = cornersMatchedCur.reshape(-1,1,2)

def denseOpticalFlow():

    pwd = os.getcwd()
    videoPath = os.path.join(pwd, "Videos", "video.mp4")
    videoCapObj = cv.VideoCapture(videoPath)

    _, frameFirst = videoCapObj.read()
    imgPrev = cv.cvtColor(frameFirst, cv.COLOR_BGR2GRAY)
    imgHSV = np.zeros_like(frameFirst)
    imgHSV[:, :, 1] = 255
    
    while True:
        ret, frameCur = videoCapObj.read()
        if not ret:
            break  
            
        imgCur = cv.cvtColor(frameCur, cv.COLOR_BGR2GRAY)
        
        # Calculate Farneback Dense Optical Flow
        flow = cv.calcOpticalFlowFarneback(
            prev=imgPrev,
            next=imgCur, 
            flow=None, 
            pyr_scale=0.5, 
            levels=3, 
            winsize=15,
            iterations=3, 
            poly_n=5, 
            poly_sigma=1.2, 
            flags=cv.OPTFLOW_FARNEBACK_GAUSSIAN
        )
     
        mag, ang = cv.cartToPolar(flow[:, :, 0], flow[:, :, 1])
        

        imgHSV[:, :, 0] = ang * 180 / np.pi / 2
        imgHSV[:, :, 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
        

        imgBGR = cv.cvtColor(imgHSV, cv.COLOR_HSV2BGR)
        cv.imshow('Video', imgBGR)
        

        if cv.waitKey(15) & 0xFF == ord('q'):
            break

        imgPrev = imgCur

    videoCapObj.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    # lucasKanade()
    denseOpticalFlow()

