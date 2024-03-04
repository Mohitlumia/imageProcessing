
import cv2
import numpy as np

# read the image
img = cv2.imread("opencv/sample_images/7grains2.jpg", 0)
pixel_size_um = 0.5

# threshold with otsu
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# clean the thresh image with erode and dilate
kernel = np.ones((3,3), np.uint8)
eroded = cv2.erode(thresh, kernel, iterations = 1)
dilated = cv2.dilate(eroded, kernel, iterations = 1)

cv2.imshow("thresh",thresh)
cv2.imshow("eroded",eroded)
cv2.imshow("dilated",dilated)
cv2.waitKey(0)