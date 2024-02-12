#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sample_images/4BSE_Google_noisy.jpg",0)

#plt.hist(img.flat,bins=256,range=(0,255))

# applying Otsu based thresholding
ret,outs = cv2.threshold(img,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)

# applying erosion
# is useful for removing small white noises
kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(outs,kernel,iterations=1)

# applying dilation
# erosion is followed by dilation in denoising
dilation = cv2.dilate(erosion,kernel,iterations=1)

# opening in cv2 is equal to erosion + dilation
opening = cv2.morphologyEx(outs,cv2.MORPH_OPEN,kernel)

# opening = erosion + dilation
# closing = dilation + erosion
closing = cv2.morphologyEx(outs,cv2.MORPH_CLOSE,kernel)

cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)
cv2.waitKey(0)
cv2.destroyAllWindows()