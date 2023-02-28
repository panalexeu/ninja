import random

import pygame

import colors
import projectile


class Gun:

    def __init__(self, init_pos, surface):
        # Stats
        self.dmg = (5, 15)
        self.ammo_capacity = 10
        self.recoil = 0
        self.fire_rate = 100

        # Gun sprite init
        self.gun_sprite = pygame.image.load('game_files/sprites/guns/gun/gun.png')
        self.gun_rect = self.gun_sprite.get_rect(topleft=init_pos)

        # Surface
        self.surface = surface

        # Positions variables
        self.x_factor = 12
        self.y_factor = -4

    def gun_pos(self, x, y):
        self.gun_rect.x = x + self.x_factor
        self.gun_rect.y = y + self.y_factor

    def shot(self, init_pos, final_pos):
        return projectile.Projectile(init_pos, final_pos, self.surface, random.randint(*self.dmg))
