
import cv2
import numpy as np

im1 = cv2.imread('opencv/sample_images/6monkey_distorted.jpg')  # read image to be registered
im2 = cv2.imread('opencv/sample_images/6monkey.jpg')            # read referance image

# convert into gray image
img1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

# Initiate ORB
orb = cv2.ORB_create(50)

# get keypoint and descripter of both images
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# Initiate Matcher
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

# match descripters of both images
matches = matcher.match(des1, des2, None)

# sort the matches based on the distance between matched descriptors
matches = sorted(matches, key = lambda x : x.distance)

############################################################
# pre processing Homography

points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches):
    points1[i,:] = kp1[match.queryIdx].pt
    points2[i,:] = kp2[match.trainIdx].pt

h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

# Use Homography

height, width, channels = im2.shape

im1Reg = cv2.warpPerspective(im1, h, (width, height))

############################################################

# draw top ten sorted matched keypoints of both images
draw_matches_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None)

cv2.imshow("Draw Matches", draw_matches_img)
cv2.imshow("Registered Image", im1Reg)
cv2.imwrite("opencv/processed_image/6Draw_Matches.jpg", draw_matches_img)
cv2.imwrite("opencv/processed_image/6Registered_Image.jpg", im1Reg)
cv2.waitKey(0)