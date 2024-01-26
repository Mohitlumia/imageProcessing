# running code in vs code with interactive window
# pip install scikit-image
#%%
from skimage import io
from matplotlib import pyplot as plt

img = io.imread("sample_images/1einstein.jpg")

plt.imshow(img, "gray")