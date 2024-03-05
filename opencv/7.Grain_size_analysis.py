
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

# convert into binary image
mask = dilated == 255

# defining structure factor
s = [[1,1,1],
     [1,1,1],
     [1,1,1]]

# assigning label to each object (grain) in binary image
from scipy import ndimage

label_mask, num_labels = ndimage.label(mask,structure=s)
# label_mask are labels on each object(grain)
# num_lables are total number of labels
# structure defines in what direction we consider the connection

# lets see the each label_mask with random color
from skimage import color

colored_labeled_img = color.label2rgb(label_mask, bg_label=0)#background color 0 (black)

#cv2.imshow("colored labeled image",colored_labeled_img)
#cv2.waitKey(0)

# now lets get the properties of our labeled grain
from skimage import measure

clusters = measure.regionprops(label_image=label_mask, intensity_image=img)
# intensity_image is optional

# clusters contains regional properties
# lets extract those properties
# clusters[0] means first grain

for grain in clusters:
    print(f"label: {grain.label} has {grain.area * pixel_size_um**2} um^2 area")

