import pygame


class Level:
    test = pygame.image.load('game_files/sprites/tiles/test.png')

    def __init__(self, surface):
        self.surface = surface

    def render(self):
        self.surface.blit(self.test, (0, 0))
