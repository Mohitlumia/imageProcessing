#%%
import cv2

img = cv2.imread("sample_images/1RGBY.jpg",1)

# cv2.imread read image as BGR blue green red
blue, green, red = cv2.split(img)

cv2.imshow("blue channel", blue)
cv2.imshow("green channel", green)
cv2.imshow("red channel", red)
cv2.waitKey(0)