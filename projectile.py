import math

import pygame


class Projectile:

    def __init__(self, init_pos, final_pos, surface, dmg):
        # Stats
        self.cooldown = 100
        self.speed = 5
        self.delta_time = 4
        self.dmg = dmg

        # Surface
        self.surface = surface

        # For calculation
        self.init_pos = init_pos
        self.final_pos = final_pos
        self.dist = None
        self.delta_x = None
        self.delta_y = None

        self.proj_sprite = pygame.image.load('game_files/sprites/projectile/fancy_proj.png')
        self.proj_rect = self.proj_sprite.get_rect(topleft=(init_pos))

    def path_calculation(self):
        rel_x = self.init_pos[0] - self.final_pos[0]
        rel_y = self.init_pos[1] - self.final_pos[1]

        # Calculates diagonal distance and angle from entity rect to destination rect
        self.dist = math.sqrt(rel_x ** 2 + rel_y ** 2)
        angle = math.atan2(-rel_y, -rel_x)

        # Divides distance to value that later gives apropriate delta x and y for the given speed
        # there needs to be at least +2 at the end for it to work with all speeds
        delta_dist = self.dist / (self.speed * self.delta_time) + 5

        # If delta_dist is greater than dist entety movement is jittery
        if delta_dist > self.dist:
            delta_dist = self.dist

        # Calculates delta x and y
        self.delta_x = math.cos(angle) * delta_dist
        self.delta_y = math.sin(angle) * delta_dist

    def move(self):
        self.path_calculation()

        if self.dist > 0:
            self.proj_rect.x += self.delta_x
            self.proj_rect.y += self.delta_y

        self.surface.blit(self.proj_sprite, (self.proj_rect.x, self.proj_rect.y))
