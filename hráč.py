import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, blockSize):
        super().__init__()
        self.image = pygame.Surface((blockSize, blockSize))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
    def get_x(self):
        x = self.rect.x
    def update(self, direction=None):
        if direction == "left":
            self.rect.x -= 5
        elif direction == "right":
            self.rect.x += 5
        elif direction == "reset":
            self.rect.x = 300
    def vybarvi(self, ola):
        if ola == 1:
            self.image.fill((255,255,25))
        elif ola == 2:
            self.image.fill((255,128,0))
        elif ola == 3:
            self.image.fill((54.5, 0, 0))
        elif ola == 4:
            self.image.fill((255, 255, 255))