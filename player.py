import pygame
from settings import WIDTH, HEIGHT, PLAYER_IMAGE

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.transform.scale(pygame.image.load("image/anjay2.png").convert_alpha(),(45,45))
        self.image_left = pygame.transform.scale(pygame.image.load("image/anjay.png").convert_alpha(),(45,45))
        self.image = self.image_right 
        self.facing_right = True
        img = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

        self.vel_y = 0
        self.gravity = 0.4
        self.speed = 3

        self.on_ground = False

    def update(self, game_started, platform):
        keys = pygame.key.get_pressed()


        if game_started:
            self.vel_y += self.gravity
        else:
            self.vel_y = 0



        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            if self.facing_right:   
                self.image = self.image_left
                self.facing_right = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            if not self.facing_right: 
                self.image = self.image_right
                self.facing_right = True

        self.rect.y += self.vel_y

        self.on_ground = False
        hits = pygame.sprite.spritecollide(self, platform, False)

        if hits and self.vel_y > 0: 
            plat = hits[0]
            self.rect.bottom = plat.rect.top
            self.vel_y = 0
            self.on_ground = True
            self.can_jump = True 

        if self.rect.top > HEIGHT:
            return False

        self.can_jump = True
        return True
    

    def jump(self):
      if self.on_ground and self.can_jump:
        self.vel_y = -13
        self.on_ground = False
        
