import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)
img_path = "./img/"

# Set game title
pygame.display.set_caption("Macross")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.player_ships = [img_path+"fighter_bat.png", img_path+"fighter_jet.png", img_path+"fighter_ger.png"]
        super().__init__()
        self.transform_ship()
        #self.image.set_colorkey(WHITE) # Set transparency color
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH / 2
        self.rect.y = WINDOW_HEIGHT / 2
        self.q_pressed = False
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        if keys[pygame.K_q] and not self.q_pressed:
            self.q_pressed = True
            # Change the ship image
            player_image = self.transform_ship()
        elif event.type == pygame.KEYUP and event.key == pygame.K_q:
            self.q_pressed = False

    
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)

    #Changes ship sprites
    def transform_ship(self):
        self.player_ships.append(self.player_ships.pop(0))
        self.image = pygame.image.load(self.player_ships[0])

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(img_path+"enemy.png").convert() # Load enemy image
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH + 10
        self.rect.y = random.randint(10, WINDOW_HEIGHT - 10)
        self.speed = random.randint(2,5)
        self.amplitude = random.randint(8,12)
        self.frequency = random.uniform(0.05, 0.1)
        self.time = 0
    
    def update(self):
        self.rect.x -= self.speed # Move the enemy to the left
        self.rect.y = self.amplitude * math.sin(self.frequency * self.time) + self.rect.y # Calculate the Y position using a sine wave)
        self.time += 1 
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(img_path+"bullet.png")
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.x += 10
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [
            pygame.image.load(img_path+"explosion1.png"),
            pygame.image.load(img_path+"explosion2.png"),
            pygame.image.load(img_path+"explosion3.png"),
            pygame.image.load(img_path+"explosion4.png")
        ]
        self.image_index = 0
        self.angle = random.randint(0, 360)
        self.image = pygame.transform.rotate(self.images[self.image_index], self.angle)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.timer = 0
        self.duration = 20 # 2 seconds in milliseconds
    
    def update(self):
        # Update timer
        self.timer += 1
        
        # Change image every 50 milliseconds
        if self.timer % 5 == 0:
            self.image_index += 1
            if self.image_index >= len(self.images):
                self.kill()
            else:
                self.image = pygame.transform.rotate(self.images[self.image_index], self.angle)
         
        # Check if the explosion has lasted for the desired duration
        if self.timer >= self.duration:
            self.kill()

### NON CLASS FUNCTIONS
# Move backgrounds
# Load background images
background_image1 = pygame.image.load(img_path+"background1.png").convert()
background_image2 = pygame.image.load(img_path+"background2.png").convert()
background1_x = 0
background2_x = WINDOW_WIDTH
def move_backgrounds(speed):
    global background1_x, background2_x
    background1_x -= speed
    background2_x -= speed
    if background1_x <= -WINDOW_WIDTH:
        background1_x = WINDOW_WIDTH
    if background2_x <= -WINDOW_WIDTH:
        background2_x = WINDOW_WIDTH

def spawn_enemies(enemies):
    if len(enemies) < 3: # Check if there are less than 3 enemies on screen
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

####
# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create player object
player = Player()
all_sprites.add(player)

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
        if enemy.rect.x < 0 or enemy.rect.y > WINDOW_HEIGHT + 50 or enemy.rect.y < -50:
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