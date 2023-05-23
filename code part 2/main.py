import pygame
import sys
from settings import *
from level import Level
from game_data import level_0

pygame.init()

FPS = 240
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(level_0, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")
    screen.fill((0, 0, 0))
    level.run()

    pygame.display.update()
    clock.tick(FPS)