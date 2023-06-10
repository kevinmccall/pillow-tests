from PIL import Image

target = "AMONGUS.jpg"

im = Image.open(target)
mask = Image.new("RGB", im.size, color=0)

r, g, b = im.split()

print(r.mode, r.size, r.palette)