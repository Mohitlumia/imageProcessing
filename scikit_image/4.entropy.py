from skimage import io
from matplotlib import pyplot as plt

img = io.imread("sample_images/4scratch.jpg")


# scratch can not be seperated using threshold based segmentation
# here entropy comes into play it uses texture to make image thresholdable

from skimage.filters.rank import entropy
from skimage.morphology import disk

entropy_img = entropy(img, disk(3))

plt.imshow(entropy_img,cmap = "gray")

# now the entropy_img can be segmented using threshold