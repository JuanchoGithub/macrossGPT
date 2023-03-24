import random
import pygame
import os
import math
import random



current_dir = os.getcwd()
print("Current working directory:", current_dir)

pygame.init()

# Create game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Macross NES Game")

# Load background images
background_image1 = pygame.image.load("background1.png").convert()
background_image2 = pygame.image.load("background2.png").convert()

# Load player image
player_ships = ["fighter_jet.png", "fighter_ger.png", "fighter_bat.png"]
player_image = pygame.transform.rotate(pygame.image.load(player_ships[0]), -90)

player_rect = player_image.get_rect()
player_rect.center = (screen_width // 2, screen_height // 2)


# Define the Enemy class
class Enemy:
    def __init__(self, screen_width, y):
        self.x = screen_width + 5
        self.y = y
        self.enemy_image = pygame.image.load("enemy.png")
        self.speed = random.randint(1,3)
        self.amplitude = random.randint(10,12)
        self.frequency =random.uniform(0.05, 0.1)

    def update(self):
        self.y += 1

    def draw(self, game_screen):
        game_screen.blit(self.enemy_image, (self.x, self.y))

    # Function to move enemies from right to left in a sine wave pattern
    def move_enemies(self, time):
        self.x -= self.speed # Move the enemy to the left
        self.y = self.amplitude * math.sin(self.frequency * time) + self.y # Calculate the Y position using a sine wave)

#Changes ship sprites
def advance_list(lst):
    if not hasattr(advance_list, 'index'):
        advance_list.index = 0
    else:
        advance_list.index += 1
        if advance_list.index >= len(lst):
            advance_list.index = 0
    new_ship = pygame.transform.rotate(pygame.image.load(lst[advance_list.index]), -90)
    return new_ship

# Function to create new enemies and add them to the screen
def create_enemies(num_enemies, game_screen):
    enemies = []
    for i in range(num_enemies):
        enemy_rect = Enemy(game_screen, screen_width, random.randint(10, screen_height-10)) # Create a new enemy rect
        enemies.append(enemy_rect)
    return enemies



def starry_background(screen, clock):
    # Set up stars
    stars = []
    for i in range(100):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        size = random.randint(1, 3)
        stars.append((x, y, size))

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        starry_background(screen, clock)
        # Clear screen
        screen.fill((0, 0, 0))

        # Draw stars
        for star in stars:
            x, y, size = star
            pygame.draw.circle(screen, (255, 255, 255), (x, y), size)

        # Flash stars
        if random.randint(0, 10) == 0:
            for i in range(10):
                x = random.randint(0, screen_width)
                y = random.randint(0, screen_height)
                size = random.randint(1, 3)
                pygame.draw.circle(screen, (255, 255, 255), (x, y), size)

        # Update display
        pygame.display.flip()
        clock.tick(60)

# Move backgrounds
background1_x = 0
background2_x = screen_width
def move_backgrounds(speed):
    global background1_x, background2_x
    background1_x -= speed
    background2_x -= speed
    if background1_x <= -screen_width:
        background1_x = screen_width
    if background2_x <= -screen_width:
        background2_x = screen_width


q_pressed = False
#enemies = create_enemies(5)
time = 0

# Set the threshold for spawning new enemies
spawn_threshold = 0.3 # 30% of enemies off screen triggers spawning

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        player_rect.move_ip(5, 0)
    if keys[pygame.K_UP]:
        player_rect.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        player_rect.move_ip(0, 5)
    if keys[pygame.K_q] and not q_pressed:
        q_pressed = True
        # Change the ship image
        player_image = advance_list(player_ships)
    elif event.type == pygame.KEYUP and event.key == pygame.K_q:
        q_pressed = False

    # Move backgrounds
    move_backgrounds(1)
    screen.blit(background_image1, (background1_x, 0))
    screen.blit(background_image2, (background2_x, 0))
    
    # Draw sprites
    screen.blit(player_image, player_rect)
    #for enemy_rect in enemy_rects:
    #    screen.blit(enemy_image, enemy_rect)
    
    # Detect collisions
#    for enemy_rect in enemy_rects:
#        if player_rect.colliderect(enemy_rect):
#            print("Collision detected!")

    time += 1


    enemies = []
    for i in range(5):
        enemies.append(Enemy(screen_width, random.randint(10, screen_height-10)))

    # Draw the enemies
    for enemy_rect in enemies:
        enemy_rect.draw(screen)

    # Check if enough enemies have gone off the screen to trigger spawning new ones
    off_screen_count = sum(1 for enemy_rect in enemies if enemy_rect.x < 0)
    if len(enemies) > 0 and off_screen_count / len(enemies) >= spawn_threshold: # Check if len(enemies) is not zero before performing division
        num_new_enemies = int(len(enemies) * 0.3) # Spawn 30% new enemies
        new_enemies = create_enemies(screen, num_new_enemies)
        enemies.extend(new_enemies)
    if len(enemies) == 0:
        new_enemies = create_enemies(screen, 10)
        enemies.extend(new_enemies)

     # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()