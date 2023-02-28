import pygame

import hp_pickup


class EnergyPickup(hp_pickup.HpPickup):

    def __init__(self, surface, init_pos):
        super().__init__(surface, init_pos)

        # Stats
        self.energy_factor = 1

        # Energy pickup sprite
        self.pickup_sprite = pygame.image.load('game_files/sprites/pickup/energy/energy.png')
        self.pickup_rect = self.pickup_sprite.get_rect(topleft=init_pos)
