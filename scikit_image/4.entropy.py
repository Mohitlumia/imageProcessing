from skimage import io
from matplotlib import pyplot as plt

img = io.imread("sample_images/4scratch.jpg")


# scratch can not be seperated using threshold based segmentation
# here entropy comes into play it uses texture to make image thresholdable

from skimage.filters.rank import entropy
from skimage.morphology import disk

entropy_img = entropy(img, disk(3))


# now the entropy_img can be segmented using threshold
# there are many threshold based segmentation let see them all

from skimage.filters import try_all_threshold

fig, ax = try_all_threshold(entropy_img,figsize=(10,8),verbose=False)
plt.show()
