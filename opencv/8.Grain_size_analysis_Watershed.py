
import cv2
import numpy as np

# read the image
img = cv2.imread("opencv/sample_images/8grains2.jpg", 0)
pixel_size_um = 0.5

# threshold with otsu
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# clean the thresh image with opening
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)

# sure background or grain boundary
sure_bg = cv2.dilate(opening,kernel,iterations=1)

# sure forground or grain boundary
dist_transform = cv2.distanceTransform(thresh,cv2.DIST_L2,3)

ret2, sure_fg = cv2.threshold(dist_transform, 0.2*dist_transform.max(), 255, 0)

sure_fg = np.uint8(sure_fg)

# unknown regions
unknown = cv2.subtract(sure_bg, sure_fg)

cv2.imshow("original image", thresh)
cv2.imshow("unknown image", unknown)
cv2.waitKey(0)