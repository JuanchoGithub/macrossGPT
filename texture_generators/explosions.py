from PIL import Image, ImageDraw

# Set image size and create new image object
width = 16
height = 16

# Create draw object for each sprite
sprite1 = ImageDraw.Draw(Image.new('RGB', (width, height), color='black'))
sprite2 = ImageDraw.Draw(Image.new('RGB', (width, height), color='black'))
sprite3 = ImageDraw.Draw(Image.new('RGB', (width, height), color='black'))
sprite4 = ImageDraw.Draw(Image.new('RGB', (width, height), color='black'))

# Draw first sprite (full orange circle)
sprite1.ellipse((0, 0, width, height), fill='orange')

# Draw second sprite (3/4 moon)
sprite2.ellipse((0, height // 4, width, height), fill='black')
sprite2.ellipse((0, 0, width, height // 2), fill='orange')

# Draw third sprite (1/2 moon)
sprite3.ellipse((0, height // 2, width, height), fill='black')
sprite3.ellipse((0, 0, width, height // 2), fill='orange')

# Draw fourth sprite (1/3 moon)
sprite4.ellipse((0, 2 * height // 3, width, height), fill='black')
sprite4.ellipse((0, 0, width, height // 3), fill='orange')

# Create new image objects and paste each sprite onto them
explosion1 = Image.new('RGB', (width, height), color='black')
explosion1.paste(sprite1.im, (0, 0, width, height))
explosion1.save('explosion1.png')

explosion2 = Image.new('RGB', (width, height), color='black')
explosion2.paste(sprite2.im, (0, 0, width, height))
explosion2.save('explosion2.png')

explosion3 = Image.new('RGB', (width, height), color='black')
explosion3.paste(sprite3.im, (0, 0, width, height))
explosion3.save('explosion3.png')

explosion4 = Image.new('RGB', (width, height), color='black')
explosion4.paste(sprite4.im, (0, 0, width, height))
explosion4.save('explosion4.png')