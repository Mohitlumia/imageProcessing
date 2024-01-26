#%%
from skimage import io
from skimage.filters import roberts, sobel, scharr, prewitt
from matplotlib import pyplot as plt

img = io.imread("sample_images/3nucleus.jpg", as_gray = True)

edge_roberts = roberts(img)
edge_sobel = sobel(img)
edge_scharr = scharr(img)
edge_prewitt = prewitt(img)

#canny is more advance filter it does edge detection and much more
#canny return a binary image
from skimage.feature import canny

#less sigma more edges
edge_canny = canny(img, sigma = 3)

plt.imshow(edge_canny, cmap = "gray")