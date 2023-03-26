from PIL import Image, ImageDraw

ancho = 32
alto = 32

img = Image.new('RGBA', (ancho, alto), (0, 0, 0, 0)) # Fondo transparente

# Dibujar un rectángulo para el torso del robot
draw = ImageDraw.Draw(img)
draw.rectangle((8, 8, 23, 23), fill=(128, 128, 128, 255))

# Dibujar los ojos del robot
draw.ellipse((10, 10, 14, 14), fill=(255, 255, 255, 255))
draw.ellipse((18, 10, 22, 14), fill=(255, 255, 255, 255))

# Dibujar la boca del robot
draw.line((16, 18, 16, 22), fill=(0, 0, 0, 255), width=2)

# Guardar la imagen en un archivo
img.save('enemy.png')