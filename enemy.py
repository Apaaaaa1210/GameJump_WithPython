import pygame
import random
from settings import WIDTH, HEIGHT

class Enemy (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("image/boal.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))

        x = random.randint(10, WIDTH-10)
        self.rect = self.image.get_rect(center=(x,-20))

        self.speed = 5

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()