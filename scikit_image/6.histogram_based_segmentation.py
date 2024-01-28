
from skimage import io, img_as_float, img_as_ubyte
from skimage.restoration import estimate_sigma, denoise_nl_means
from matplotlib import pyplot as plt
import numpy as np

img = img_as_float(io.imread("sample_images/6BSE_Google_noisy.jpg"))

# denoising using nlm_denoising_filter

sigma_est = np.mean(estimate_sigma(img, channel_axis=-1))

nlm_img = denoise_nl_means(img,h = 1.15*sigma_est, fast_mode=True, patch_size=5, patch_distance=3)
nlm_ubyte_img = img_as_ubyte(nlm_img)

# picking segments based on peeks shown in the histogram
# creating binary image of each segment
segm1 = (nlm_ubyte_img <= 27)
segm2 = (27 < nlm_ubyte_img) & (nlm_ubyte_img <= 55)
segm3 = (55 < nlm_ubyte_img) & (nlm_ubyte_img <= 95)
segm4 = (95 < nlm_ubyte_img) & (nlm_ubyte_img <= 125)
segm5 = (125 < nlm_ubyte_img) & (nlm_ubyte_img <= 200)
segm6 = (200 < nlm_ubyte_img)

# assign differnt color to each segment
all_segm = np.zeros((nlm_ubyte_img.shape[0], nlm_ubyte_img.shape[1], 3))

all_segm[segm1] = (1,0,0)
all_segm[segm2] = (0,1,0)
all_segm[segm3] = (0,0,1)
all_segm[segm4] = (1,1,0)
all_segm[segm5] = (0,1,1)
all_segm[segm6] = (1,0,1)

plt.imshow(all_segm)
