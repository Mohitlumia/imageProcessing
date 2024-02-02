import cv2
import numpy as np

img = cv2.imread("sample_images/2BSE_Google_noisy.jpg", 1)

# creating my own bluring filter
kernel = np.ones((3,3),np.float32)/9
filter_2D = cv2.filter2D(img,-1,kernel)

cv2.imshow("Custom filter", filter_2D)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()