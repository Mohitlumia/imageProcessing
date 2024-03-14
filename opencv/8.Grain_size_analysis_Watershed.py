
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

ret2, sure_fg = cv2.threshold(dist_transform, 0.1*dist_transform.max(), 255, 0)

sure_fg = np.uint8(sure_fg)

# unknown regions
unknown = cv2.subtract(sure_bg, sure_fg)

# markers
ret3, markers = cv2.connectedComponents(sure_fg)

markers = markers+10

markers[unknown==255] = 0

markers = cv2.watershed(img_color,markers)

img_color[markers == -1] = [0,0,255]

# color each grain
img_grain_color = color.label2rgb(markers, bg_label=0)

cv2.imshow("watershed", img_color)
cv2.imshow("colored grains",img_grain_color)
cv2.waitKey(0)

cv2.imwrite("opencv/processed_image/8Grain_Analysis/8watershed.jpg", img_color)

# now lets get the properties of our labeled grain
from skimage import measure

clusters = measure.regionprops(label_image=markers, intensity_image=img)
# intensity_image is optional

# clusters contains regional properties
# lets extract those properties
# clusters[0] means first grain

propList = ['Area',
            'equivalent_diameter', #Added... verify if it works
            'orientation', #Added, verify if it works. Angle btwn x-axis and major axis.
            'MajorAxisLength',
            'MinorAxisLength',
            'Perimeter',
            'MinIntensity',
            'MeanIntensity',
            'MaxIntensity']

output_file = open("opencv/processed_image/8Grain_Analysis/8image_measurements.csv", "w")
output_file.write(',' + ",".join(propList) + '\n') #join strings in array by commas, leave first cell blank
#First cell blank to leave room for header (column names)

for grain in clusters:
    #output cluster properties to the excel file
    output_file.write(str(grain['Label']))
    for i,prop in enumerate(propList):
        if(prop == 'Area'):
            #Convert pixel square to um square
            to_print = grain[prop]*pixel_size_um**2
        elif(prop == 'orientation'):
            #Convert to degrees from radians
            to_print = grain[prop]*57.2958
        elif(prop.find('Intensity') < 0):
            # intensity properties
            to_print = grain[prop]*pixel_size_um
        else:
            #Reamining props
            to_print = grain[prop]
        output_file.write(',' + str(to_print))
    output_file.write('\n')
output_file.close()