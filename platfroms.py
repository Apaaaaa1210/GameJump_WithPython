import pygame
from settings import PLATFORM_IMAGE

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        img = pygame.image.load(PLATFORM_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(img, (70, 20))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dy):
        self.rect.y += dy

        if self.rect.top > 600:
            self.kill()
