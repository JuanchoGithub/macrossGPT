import pygame
import random
from classes.game_context import IMG_PATH

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [
            pygame.image.load(IMG_PATH+"explosion1.png"),
            pygame.image.load(IMG_PATH+"explosion2.png"),
            pygame.image.load(IMG_PATH+"explosion3.png"),
            pygame.image.load(IMG_PATH+"explosion4.png")
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

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))