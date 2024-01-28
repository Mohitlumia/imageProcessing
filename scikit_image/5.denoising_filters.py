from skimage import io
import matplotlib.pyplot as plt

img = io.imread("sample_images/5noisy_img.jpg")

# we may not be able to compare original and processed image
# so lets save them in a separate folder name processed_images

plt.imsave("processed_images/5original.jpg",img)