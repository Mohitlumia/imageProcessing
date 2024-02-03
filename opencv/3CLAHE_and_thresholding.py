# CLAHE contrast limiting histogram equalization
import cv2
import numpy as np

img = cv2.imread("opencv/sample_images/3Alloy.jpg",0)

# equalize img or stratches histogram
eq_img = cv2.equalizeHist(img)

# eq_img is very noisy as it's equlized globly
# for equalizing localy we use CALHE
clhe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl_img = clhe.apply(img)

cv2.imshow("Original image", img)
cv2.imshow("Equalized image", eq_img)
cv2.imshow("CLHE image", cl_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
