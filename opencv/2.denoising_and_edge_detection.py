import cv2
import numpy as np

img = cv2.imread("sample_images/2BSE_Google_noisy.jpg", 1)

# creating my own bluring filter
kernel = np.ones((3,3),np.float32)/9
filter_2D = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(3,3))
gaussian_blur = cv2.GaussianBlur(img, (3,3),0) # sigma = 0
median_blur = cv2.medianBlur(img,3)
# bilateral blur denoise img and preserve edges better than median
bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Bilateral blur", bilateral_blur)
cv2.imshow("Median blur", median_blur)
cv2.imshow("Gaussian blur", gaussian_blur)
cv2.imshow("Blur", blur)
cv2.imshow("Custom filter", filter_2D)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()