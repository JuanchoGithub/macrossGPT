from PIL import Image, ImageDraw

# Set up image size and background color
width = 64
height = 64
bg_color = (0, 0, 0, 0)

# Create image and drawing context
img = Image.new('RGBA', (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Draw ship on image
body_color = (255, 0, 0)
wing_color = (0, 128, 128)
window_color = (255, 255, 255)
ship_pos = (width // 2, height - 24)
ship_size = 24
wing_size = 10
wing_offset = 2
draw.polygon([(ship_pos[0], ship_pos[1] - ship_size),
              (ship_pos[0] - wing_size, ship_pos[1] - wing_offset),
              (ship_pos[0] - wing_size // 2, ship_pos[1] - wing_offset),
              (ship_pos[0] - wing_size // 2, ship_pos[1] + ship_size // 2),
              (ship_pos[0] + wing_size // 2, ship_pos[1] + ship_size // 2),
              (ship_pos[0] + wing_size // 2, ship_pos[1] - wing_offset),
              (ship_pos[0] + wing_size, ship_pos[1] - wing_offset)], fill=wing_color)
draw.polygon([(ship_pos[0] - wing_size // 2, ship_pos[1] + ship_size // 2),
              (ship_pos[0] + wing_size // 2, ship_pos[1] + ship_size // 2),
              (ship_pos[0], ship_pos[1])], fill=body_color)
draw.ellipse((ship_pos[0] - ship_size // 4, ship_pos[1] - ship_size,
              ship_pos[0] + ship_size // 4, ship_pos[1]), fill=window_color)

# Save image as PNG file
img.save("fighter_jet.png", format='PNG')
