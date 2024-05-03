import pygame
import random

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, imagePath, blockSize):
        super().__init__()
        self.image = pygame.Surface((blockSize, blockSize))
        self.image.fill((255, 0, 0))  # červený čtvereček místo obrázku pro jednoduchost
        self.rect = self.image.get_rect(center=(x, y))
    def update(self):
        self.rect.y += 5
