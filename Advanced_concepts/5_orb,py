import cv2 as cv
import matplotlib.pyplot as plt
import os

def orb_detection():
    # Step 1: Find and Load the Image in Grayscale
    pwd = os.getcwd()
    imgPath = os.path.join(pwd, 'tesla.png')
    imgGray = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    
    # Step 2: Create the Tool (ORB instead of SIFT)
    # nfeatures=500 tells ORB to only keep the top 500 best landmarks
    orb = cv.ORB_create(nfeatures=150, scaleFactor=1.2, nlevels=4)
    
    # Step 3: Find the Points (Detect)
    keypoints = orb.detect(imgGray, None)
    
    # Step 4: Visualizing the Results (Draw Rich Keypoints)
    img_with_keypoints = cv.drawKeypoints(
        imgGray, 
        keypoints, 
        None, 
        flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )

    # Plot the final image
    plt.figure(figsize=(10, 6))
    plt.imshow(img_with_keypoints)
    plt.title("ORB Keypoints")
    plt.show()

if __name__ == "__main__":
    orb_detection()