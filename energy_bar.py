import pygame

import hp_bar

class EnergyBar(hp_bar.HpBar):

    def __init__(self, surface, init_pos):
        super().__init__(surface, init_pos)
        self.tile = pygame.image.load('game_files/sprites/bar/energy/coffe.png')
