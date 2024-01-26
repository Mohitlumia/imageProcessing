#%%
import cv2

img = cv2.imread("sample_images/1einstein.jpg")

cv2.imshow("einstein original image", img)
cv2.waitKey(0)