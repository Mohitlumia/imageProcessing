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

cv2.imshow("Harris", img)
cv2.waitKey(0)
