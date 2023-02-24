import pygame

import projectile


class Gun:

    def __init__(self):
        # Stats
        self.damage = 10
        self.ammo_capacity = 10
        self.recoil = 30
        self.gun_sprite = pygame.image.load('game_files/sprites/test/gun_1.png')

    def shot(self, init_pos, final_pos, surface):
        return projectile.Projectile(init_pos, final_pos, surface)

