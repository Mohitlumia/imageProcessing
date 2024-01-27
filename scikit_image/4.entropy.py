from skimage import io
from matplotlib import pyplot as plt

img = io.imread("sample_images/4scratch.jpg")

plt.imshow(img, cmap = "gray")

# scratch can not be seperated using threshold based segmentation
