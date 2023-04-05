import pygame
from classes.player import Player
from classes.explosion import Explosion
from classes.enemy import Enemy
from classes.game_context import all_sprites, enemies, bullets, screen, IMG_PATH  



# Initialize Pygame
pygame.init()

# Create player object
player = Player()
all_sprites.add(player)

# Set game title
pygame.display.set_caption("Macross")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

### NON CLASS FUNCTIONS
# Move backgrounds
# Load background images
background_image1 = pygame.image.load(IMG_PATH+"background1.png").convert()
background_image2 = pygame.image.load(IMG_PATH+"background2.png").convert()
background1_x = 0
background2_x = screen.get_width()
def move_backgrounds(speed):
    global background1_x, background2_x
    background1_x -= speed
    background2_x -= speed
    if background1_x <= -screen.get_width():
        background1_x = screen.get_width()
    if background2_x <= -screen.get_width():
        background2_x = screen.get_width()

def spawn_enemies(enemies):
    if len(enemies) < 3: # Check if there are less than 3 enemies on screen
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)


# Set up game loop
running = True
clock = pygame.time.Clock()

# Other variables
time = 0
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    
    spawn_enemies(enemies)

    # Update game state
    all_sprites.update() 
    for enemy in enemies:
        if enemy.rect.x < 0 or enemy.rect.y > screen.get_height() + 50 or enemy.rect.y < -50:
            enemies.remove(enemy)
            all_sprites.remove(enemy)
    
    # Check for collisions
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        enemy = Enemy()
        #all_sprites.add(enemy)
        #enemies.add(enemy)
        all_sprites.add(Explosion(hit.rect.x, hit.rect.y))
    
    hits = pygame.sprite.spritecollide(player, enemies, False) 
    if hits:
        running = False
    
    # Draw game objects
    # Move backgrounds
    move_backgrounds(1)
    screen.blit(background_image1, (background1_x, 0))
    screen.blit(background_image2, (background2_x, 0))


    all_sprites.draw(screen)
    
    # Flip display
    pygame.display.flip()
    
    # Set game speed
    clock.tick(60)
    time += 1

# Quit Pygame
pygame.quit()