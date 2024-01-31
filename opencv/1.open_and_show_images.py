#%%
import cv2

img = cv2.imread("sample_images/1einstein.jpg",0)
# second arg in cv.imread 0,1,2 represents gray, colour and alpha channel
# print(img.shape)
cv2.imshow("einstein original image", img)
cv2.waitKey(0)