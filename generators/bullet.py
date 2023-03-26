from PIL import Image, ImageDraw

# Set image size and create new image object
width = 8
height = 16
img = Image.new('RGB', (width, height), color='black')

# Create draw object
draw = ImageDraw.Draw(img)

# Draw yellow stripes
draw.rectangle((0, 0, width, 4), fill='yellow')
draw.rectangle((0, 12, width, height), fill='yellow')

# Draw white center
draw.rectangle((0, 4, width, 12), fill='white')

# Save image
img.save('bullet.png')