from skimage import io
import matplotlib.pyplot as plt

img = io.imread("sample_images/5noisy_img.jpg")

# we may not be able to compare original and processed image
# so lets save them in a separate folder name processed_images

# now lets apply gaussian filter to denoise our original image

from scipy import ndimage as nd

gaussian_img = nd.gaussian_filter(img, sigma = 3)
# sigma represents standard deviation from mean
# sigma 1 = 68%, sigma 2 = 95% and sigma 3 = 99.7%

plt.imsave("processed_images/5gaussian.jpg", gaussian_img)