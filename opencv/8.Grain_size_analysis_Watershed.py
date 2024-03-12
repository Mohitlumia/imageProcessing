
import cv2
import numpy as np
from skimage import color
from skimage.segmentation import clear_border

# read the image
img_color = cv2.imread("opencv/sample_images/8grains2.jpg")
img = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)
pixel_size_um = 0.5

# threshold with otsu
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# clean the thresh image with opening
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)

# clear grains that are touching border
opening = clear_border(opening)

# sure background or grain boundary
sure_bg = cv2.dilate(opening,kernel,iterations=2)

# sure forground or grain boundary
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,3)

ret2, sure_fg = cv2.threshold(dist_transform, 0.2*dist_transform.max(), 255, 0)

sure_fg = np.uint8(sure_fg)

# unknown regions
unknown = cv2.subtract(sure_bg, sure_fg)

# markers
ret3, markers = cv2.connectedComponents(sure_fg)

markers = markers+10

markers[unknown==255] = 0

markers = cv2.watershed(img_color,markers)

img_color[markers == -1] = [255,0,0]

# color each grain
img_grain_color = color.label2rgb(markers, bg_label=0)

cv2.imshow("threshold image", thresh)
cv2.imshow("watershed", img_color)
cv2.imshow("colored grains",img_grain_color)
cv2.waitKey(0)