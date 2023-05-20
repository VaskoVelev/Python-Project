import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((55,55,55))
        self.rect = self.image.get_rect(topleft = position)