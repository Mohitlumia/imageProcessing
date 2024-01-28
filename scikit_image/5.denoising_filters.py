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

#%%
# now lets apply median filter to denoise our orignal image

median_img = nd.median_filter(img, size = 3)
# size of the window of the kernal

plt.imsave("processed_images/5median.jpg",median_img)

#%%
# now lets apply non-local means denoising filter

import numpy as np
from skimage.restoration import estimate_sigma, denoise_nl_means

# well lets see how its gonna work with float img
from skimage import img_as_float

sigma_est = np.mean(estimate_sigma(img_as_float(img), channel_axis=-1))
# channel_axis is color axis

nlm_img = denoise_nl_means(img,h = 1.15*sigma_est, fast_mode=True, patch_size=5, patch_distance=3, channel_axis=-1)
# if fast_mode is False it will take atlest a order of megnitude difference

plt.imsave("processed_images/5non_local_means.jpg", nlm_img)