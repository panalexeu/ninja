import math

import pygame

class Projectile:

    def __init__(self, init_pos, final_pos, surface):
        # Stats
        self.speed = 1
        self.delta_time = 4

        # Surface
        self.surface = surface

        self.init_pos = init_pos
        self.final_pos = final_pos
        self.projectile_sprite = pygame.image.load('game_files/sprites/test/cursor.png')

    def move(self):
        rel_x = self.init_pos[0] - self.final_pos[0]
        rel_y = self.init_pos[1] - self.final_pos[1]

        # Calculates diagonal distance and angle from entity rect to destination rect
        dist = math.sqrt(rel_x ** 2 + rel_y ** 2)
        angle = math.atan2(-rel_y, -rel_x)

        # Divides distance to value that later gives apropriate delta x and y for the given speed
        # there needs to be at least +2 at the end for it to work with all speeds
        delta_dist = dist / (self.speed * self.delta_time) + 5

        # If delta_dist is greater than dist entety movement is jittery
        if delta_dist > dist:
            delta_dist = dist

        # Calculates delta x and y
        delta_x = math.cos(angle) * (delta_dist)
        delta_y = math.sin(angle) * (delta_dist)

        if dist > 0:
            self.init_pos[0] += delta_x
            self.init_pos[1] += delta_y

        self.surface.blit(self.projectile_sprite, (self.init_pos[0], self.init_pos[1]))
