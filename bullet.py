import pygame

'''use sprite, so we an manage bullets altogether'''
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__() #inheritance Bullet from Sprite
        self.screen = screen

        #Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) #x,y of top left
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''Move the bullet up the screen'''
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        '''draw bullet onto the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)
