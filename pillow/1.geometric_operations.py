
from PIL import Image

image = Image.open("pillow/sample_images/1lenna.png")

## Resize

width,height = image.size
new_width = 2 * width
new_hight = height
resize_image = image.resize((new_width, new_hight))

resize_image.save("pillow/processed_images/1resize_lenna.png")
