#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sample_images/4BSE_Google_noisy.jpg",0)

plt.hist(img.flat,bins=256,range=(0,255))

# applying Otsu based thresholding
ret,outs = cv2.threshold(img,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)

cv2.imshow("Original image", img)
cv2.imshow("Otsu",outs)
cv2.waitKey(0)
cv2.destroyAllWindows()