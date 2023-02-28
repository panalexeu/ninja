import pygame

import gun


class Revolver(gun.Gun):

    def __init__(self, init_pos, surface):
        super().__init__(init_pos, surface)

        # Stats
        self.dmg = (50, 200)
        self.fire_rate = 600

        # Gun sprite init
        self.gun_sprite = pygame.image.load('game_files/sprites/guns/revolver/revolver.png')
        self.gun_rect = self.gun_sprite.get_rect(topleft=init_pos)
