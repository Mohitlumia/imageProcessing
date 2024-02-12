#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sample_images/4BSE_Google_noisy.jpg",0)

plt.hist(img.flat,bins=256,range=(0,255))

# applying Otsu based thresholding
ret,outs = cv2.threshold(img,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)

# applying erosion
# is useful for removing small white noises
kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(outs,kernel,iterations=1)

# applying dilation
# erosion is followed by dilation in denoising
dilation = cv2.dilate(erosion,kernel,iterations=1)

cv2.imshow("Original image", img)
cv2.imshow("Otsu",outs)
cv2.imshow("Erosion image",erosion)
cv2.imshow("Erosion+Dilation image",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()