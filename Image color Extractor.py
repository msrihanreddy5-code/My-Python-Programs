from collections import Counter
from PIL import Image

img = Image.open("your_image.jpg")
pixels = list(img.getdata())
top = Counter(pixels).most_common(5)

print("Top Colors:", top)
