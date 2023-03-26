from PIL import Image, ImageDraw

# Set up image size and background color
width = 64
height = 64
bg_color = (0, 0, 0, 0)

# Create image and drawing context for GERWALK
img_gerwalk = Image.new('RGBA', (width, height), bg_color)
draw_gerwalk = ImageDraw.Draw(img_gerwalk)

# Draw GERWALK on image
body_color = (255, 0, 0)
wing_color = (0, 128, 128)
window_color = (255, 255, 255)
ship_pos = (width // 2, height - 24)
ship_size = 24
wing_size = 10
leg_size = 6
wing_offset = 2
draw_gerwalk.polygon([(ship_pos[0], ship_pos[1] - ship_size),
                      (ship_pos[0] - wing_size, ship_pos[1] - wing_offset),
                      (ship_pos[0] - wing_size // 2, ship_pos[1] - wing_offset),
                      (ship_pos[0] - wing_size // 2, ship_pos[1] + ship_size // 4),
                      (ship_pos[0], ship_pos[1] + ship_size // 2),
                      (ship_pos[0] + wing_size // 2, ship_pos[1] + ship_size // 4),
                      (ship_pos[0] + wing_size // 2, ship_pos[1] - wing_offset),
                      (ship_pos[0] + wing_size, ship_pos[1] - wing_offset)], fill=wing_color)
draw_gerwalk.rectangle((ship_pos[0] - leg_size, ship_pos[1] + ship_size // 4,
                         ship_pos[0] + leg_size, height - leg_size), fill=body_color)
draw_gerwalk.line((ship_pos[0] - leg_size, ship_pos[1] + ship_size // 4,
                   ship_pos[0] - leg_size // 2, height - leg_size), fill=wing_color, width=2)
draw_gerwalk.line((ship_pos[0] + leg_size, ship_pos[1] + ship_size // 4,
                   ship_pos[0] + leg_size // 2, height - leg_size), fill=wing_color, width=2)
draw_gerwalk.ellipse((ship_pos[0] - ship_size // 4, ship_pos[1] - ship_size,
                      ship_pos[0] + ship_size // 4, ship_pos[1]), fill=window_color)

# Save image as PNG file for GERWALK
img_gerwalk.save("fighter_ger.png", format='PNG')