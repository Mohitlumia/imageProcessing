#%%
from skimage import io
from skimage.transform import rescale, resize, downscale_local_mean

img = io.imread("sample_images/2monkey.jpg", as_gray = True)

#anti_aliasing increase sharpness
rescal_img = rescale(img,1.0/4.0, anti_aliasing = True)
resize_img = resize(img,(200,200),anti_aliasing = True)
downscale_img = downscale_local_mean(img,(1,3))

plt.imshow(downscale_img, "gray")