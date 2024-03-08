
from PIL import Image
import numpy as np
import cv2

image = Image.open("pillow/sample_images/1lenna.png")

## Resize

width,height = image.size
new_width = 2 * width
new_hight = height
resize_image = image.resize((new_width, new_hight))

resize_image.save("pillow/processed_images/1resize_lenna.png")

## Rotate

theta = 45
rotate_image = image.rotate(theta)

rotate_image.save("pillow/processed_images/1rotate_lenna.png")

