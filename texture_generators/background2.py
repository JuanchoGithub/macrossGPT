from PIL import Image, ImageDraw
import random

# Set up image size and background color
width = 800
height = 600
bg_color = (0, 0, 0, 0)

# Set up stars
num_stars = 340
star_colors = [(255, 255, 255), (255, 255, 200), (255, 255, 150), (255, 255, 100)]
stars = []
for i in range(num_stars):
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.randint(1, 3)
    color = random.choice(star_colors)
    stars.append((x, y, size, color))

# Draw stars on image
img = Image.new('RGBA', (width, height), bg_color)
draw = ImageDraw.Draw(img)
for star in stars:
    x, y, size, color = star
    draw.ellipse((x, y, x+size, y+size), fill=color)

# Save image as PNG file with alpha channel
img.save("temp_background2.png", format='PNG', save_all=True, optimize=True)

# Save alpha channel as separate PNG file
alpha = img.split()[-1]
alpha.save("background2.png")