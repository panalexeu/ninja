import pygame


class HpBar:

    def __init__(self, surface, init_pos):
        self.surface = surface
        self.init_pos = init_pos
        self.no_tile = pygame.image.load('game_files/sprites/bar/heart/no_heart.png')
        self.tile = pygame.image.load('game_files/sprites/bar/heart/heart.png')

    def render(self, items_count, scale_factor):
        for index in range(5):
            if index < items_count:
                self.surface.blit(pygame.transform.scale_by(self.tile, scale_factor),
                                  (self.init_pos[0] + index * scale_factor * 9, self.init_pos[1]))
            else:
                self.surface.blit(pygame.transform.scale_by(self.no_tile, scale_factor),
                                  (self.init_pos[0] + index * scale_factor * 9, self.init_pos[1]))
