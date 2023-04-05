import pygame
from classes.game_context import IMG_PATH

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(IMG_PATH+"bullet.png")
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 20
    
    def update(self):
        self.rect.x += 10
        if self.rect.y < 0:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))