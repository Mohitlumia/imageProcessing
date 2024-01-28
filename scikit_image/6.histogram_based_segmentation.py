
from skimage import io, img_as_float, img_as_ubyte
from skimage.restoration import estimate_sigma, denoise_nl_means
from matplotlib import pyplot as plt
import numpy as np

img = img_as_float(io.imread("sample_images/6BSE_Google_noisy.jpg"))

# denoising using nlm_denoising_filter

sigma_est = np.mean(estimate_sigma(img, channel_axis=-1))

nlm_img = denoise_nl_means(img,h = 1.15*sigma_est, fast_mode=True, patch_size=5, patch_distance=3)
nlm_ubyte_img = img_as_ubyte(nlm_img)

plt.hist(nlm_ubyte_img.flat,bins=100, range=(0,255))
