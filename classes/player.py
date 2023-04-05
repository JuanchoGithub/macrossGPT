import pygame
from .bullet import Bullet
from classes.game_context import bullets, all_sprites, screen, IMG_PATH

# Define classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.player_ships = [IMG_PATH+"fighter_bat.png", IMG_PATH+"fighter_jet.png", IMG_PATH+"fighter_ger.png"]
        super().__init__()
        self.img_path = IMG_PATH
        self.transform_ship()
        #self.image.set_colorkey(WHITE) # Set transparency color
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2
        self.rect.y = screen.get_height() / 2
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
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_q:
                self.q_pressed = False
        self.rect.x = screen.get_width() if self.rect.x >= screen.get_width() else  self.rect.x
        self.rect.x = 0 if self.rect.x < 0 else self.rect.x
        self.rect.y = screen.get_height()- 60 if self.rect.y >= screen.get_height() - 60 else self.rect.y
        self.rect.y = 0 if self.rect.y < 0 else self.rect.y

    
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)

    #Changes ship sprites
    def transform_ship(self):
        self.player_ships.append(self.player_ships.pop(0))
        self.image = pygame.image.load(self.player_ships[0])
