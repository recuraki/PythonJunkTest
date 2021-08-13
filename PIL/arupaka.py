from PIL import Image, ImageChops

img = Image.open("animal_arupaka.png")

r, g, b = img.split()
