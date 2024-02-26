
import cv2


im1 = cv2.imread('opencv/sample_images/6monkey.jpg')            # read referance image
im2 = cv2.imread('opencv/sample_images/6monkey_distorted.jpg')  # read image to be registered

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

# draw top ten sorted matched keypoints of both images
draw_matches_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None)

cv2.imshow("Draw Matches", draw_matches_img)
cv2.waitKey(0)