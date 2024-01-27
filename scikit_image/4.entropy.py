from skimage import io
from matplotlib import pyplot as plt

img = io.imread("sample_images/4scratch.jpg")


# scratch can not be seperated using threshold based segmentation
# here entropy comes into play it uses texture to make image thresholdable

from skimage.filters.rank import entropy
from skimage.morphology import disk

entropy_img = entropy(img, disk(3))


# now the entropy_img can be segmented using threshold
# lets apply otsu threshold as it showed comparetively batter result

from skimage.filters import threshold_otsu

threshold_val = threshold_otsu(entropy_img)
# now as we have threshold value can use it to make a binary image

binary_img = entropy_img <= threshold_val

plt.imshow(binary_img,cmap="gray")
