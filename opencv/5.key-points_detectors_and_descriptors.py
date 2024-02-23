#Harris

import cv2
import numpy as np

img = cv2.imread("opencv/sample_images/5grains.jpg")

# Harris works on gray image of float32 type
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

harris = cv2.cornerHarris(gray,2,3,0.04)

# keeping only one percent of harris.max()
img[harris>0.01*harris.max()] = [225,0,0]

#cv2.imshow("Harris", img)
#cv2.waitKey(0)

####################################################

# Good Features to Track

img = cv2.imread("opencv/sample_images/5grains.jpg")

# it detectes corners of features in the image
corners = cv2.goodFeaturesToTrack(gray,maxCorners=50,qualityLevel=0.01,minDistance=10)

# it output the coordinate of corner points
corners = np.int0(corners)

# iterating throght each point and puting circle
for coordinate in corners:
    x,y = coordinate.ravel()
    cv2.circle(img,(x,y),3,255,-1)

#cv2.imshow("Corner",img)
#cv2.waitKey(0)

###################################################
    
# Fast Feature Detector

img = cv2.imread("opencv/sample_images/5grains.jpg")

# initiate FAST object with default values
detector = cv2.FastFeatureDetector_create()

kp = detector.detect(img)

img2 = cv2.drawKeypoints(img,kp,None,flags=0)

#cv2.imshow("Corners", img2)
#cv2.waitKey(0)

###################################################

# ORB
# it contains both the detector(FAST) and descriptor(BRIEF)

img = cv2.imread("opencv/sample_images/5grains.jpg")

orb = cv2.ORB_create(50)

kp, des = orb.detectAndCompute(img,None)

img2 = cv2.drawKeypoints(img,kp,None,flags=0)

cv2.imshow("ORB", img2)
cv2.waitKey(0)



