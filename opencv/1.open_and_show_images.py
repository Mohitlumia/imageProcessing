#%%
import cv2

img = cv2.imread("sample_images/1RGBY.jpg",1)

# cv2.imread read image as BGR blue green red
blue, green, red = cv2.split(img)

merged_channels = cv2.merge((blue,green,red))

cv2.imshow("merged_img", merged_channels)
cv2.waitKey(0)