import pygame
import random
from settings import WIDTH, HEIGHT, BACKGROUND_IMAGE
from player import Player
from platfroms import Platform
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Game")


bg = pygame.image.load(BACKGROUND_IMAGE).convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

clock = pygame.time.Clock()


MAX_PLATFORM = 6
MIN_GAP = 60
MAX_GAP = 120

MAX_ENEMIES = 5
MIN_DISTANCE = 60


all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()


player = Player(WIDTH // 2, HEIGHT - 70)
all_sprites.add(player)

start_platform = Platform(WIDTH // 2, HEIGHT - 20)
platforms.add(start_platform)
all_sprites.add(start_platform)

START_OFFSET = 190
for i in range(6):
    p = Platform(
        random.randint(20, WIDTH - 20),
        HEIGHT - START_OFFSET - i * 120
    )
    platforms.add(p)
    all_sprites.add(p)


game_started = False
running = True
game_over = False
fade_alpha = 0

enemy_timer = 0
enemy_spawn_interval = 40  


def spawn_enemy(enemies_group, all_sprites_group):
    if len(enemies_group) >= MAX_ENEMIES:
        return  
    max_attempts = 10
    for _ in range(max_attempts):
        x = random.randint(20, WIDTH-20)
        too_close = False
        for e in enemies_group:
            if abs(e.rect.x - x) < MIN_DISTANCE:
                too_close = True
                break
        if not too_close:
            e = Enemy()
            e.rect.x = x
            enemies_group.add(e)
            all_sprites_group.add(e)
            break

while running:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
                game_started = True

    alive = player.update(game_started, platforms)
    if not alive:
        game_over = True  


    if game_over:
        fade_alpha = min(fade_alpha + 5, 255)
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        if fade_alpha > 150:
            font = pygame.font.SysFont("Arial", 30, bold=True)
            text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

        pygame.display.update()
        continue


    enemy_timer += 1
    if enemy_timer >= enemy_spawn_interval:
        enemy_timer = 0
        spawn_enemy(enemies, all_sprites)

    enemies.update()

    if pygame.sprite.spritecollide(player, enemies, False):
        print("TERKENA MUSUH — GAME OVER")
        game_over = True

    hits = pygame.sprite.spritecollide(player, platforms, False)
    if hits and player.vel_y > 0:
        player.rect.bottom = hits[0].rect.top
        player.vel_y = 0


    if player.rect.top <= HEIGHT / 3:
        dy = abs(player.vel_y)
        for plat in platforms:
            plat.update(dy)

        if len(platforms) < MAX_PLATFORM:
            highest = min([p.rect.y for p in platforms])
            gap = random.randint(MIN_GAP, MAX_GAP)
            new_y = highest - gap
            new_x = random.randint(20, WIDTH - 20)

            p = Platform(new_x, new_y)
            platforms.add(p)
            all_sprites.add(p)

    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
