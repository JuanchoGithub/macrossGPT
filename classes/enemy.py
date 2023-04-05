import pygame
import random
import math
from classes.game_context import screen, IMG_PATH, all_sprites

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(IMG_PATH+"enemy.png").convert() # Load enemy image
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() + 10
        self.rect.y = random.randint(10, screen.get_height() - 10)
        self.speed = random.randint(2,7)
        self.movement_width = random.randint(30,60)
        self.movement_zig_width = random.randint(20, 50)
        self.movement_speed = random.uniform(0.03, 0.08)
        self.radius = 100
        self.angle = 0
        self.angle_increment = 0.01        
        self.time = 0
        # Choose a random function to run during initialization
        self.chosen_function = random.choice([self.straight_movement, 
                                              self.zigzag_movement, 
                                              self.sine_wave_movement, 
                                              self.circular_movement, 
                                              self.diving_movement])

    def update(self):
        self.chosen_function()
        #self.rect.x -= self.speed # Move the enemy to the left
        #self.rect.y = self.amplitude * math.sin(self.frequency * self.time) + self.rect.y # Calculate the Y position using a sine wave)
        #self.time += 1 

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


    #Straight movement:
    def straight_movement(self):
        self.rect.x -= self.speed
        return self.rect.x, self.rect.y
    
    #Zigzag movement:
    def zigzag_movement(self):
        self.rect.x -= self.speed
        self.rect.y += self.movement_zig_width * math.sin(self.movement_speed * self.rect.x)
        return self.rect.x, self.rect.y
    #Note: This function requires the math module to be imported.

    #Sine wave movement:
    def sine_wave_movement(self):
        self.rect.x -= self.speed
        self.rect.y += self.movement_width * math.sin(self.movement_speed * self.rect.x)
        return self.rect.x, self.rect.y
    #Note: This function also requires the math module to be imported.

    #Circular movement:
    def circular_movement(self):
        # Calculate the new x and y positions based on the angle and radius
        self.angle -= self.speed
        self.rect.x = self.rect.x - self.speed * math.cos(self.angle * math.pi / 180)
        self.rect.y = self.rect.y - self.speed * math.sin(self.angle * math.pi / 180)
        self.rect.x -= self.speed

    #Diving movement:
    def diving_movement(self):
        for sprite in all_sprites:
            if hasattr(sprite, "__module__") and sprite.__module__ == 'classes.player':
                player = sprite
                self.rect.x -= self.speed
                self.rect.y += (player.rect.y - self.rect.y) * self.speed / (abs(player.rect.y - self.rect.y) + 1)
                self.rect.y += self.movement_speed

        return self.rect.x, self.rect.y
