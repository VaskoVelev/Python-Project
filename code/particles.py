import pygame
from support import import_folder
from settings import graphics_color

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, position, type):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.15
        if type == "jump":
            self.frames = import_folder(f"Python-Project/graphics/{graphics_color}_graphics/character/dust_particles/jump")
        if type == "land":
            self.frames = import_folder(f"Python-Project/graphics/{graphics_color}_graphics/character/dust_particles/land")
        if type == "explosion":
            self.frames = import_folder(f"Python-Project/graphics/{graphics_color}_graphics/enemy/explosion")
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = position)
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, shift):
        self.animate()
        self.rect.x += shift