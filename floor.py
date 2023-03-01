import pygame

import wall


class Floor(wall.Wall):

    def __init__(self, surface, init_pos, angle):
        super().__init__(surface, init_pos, angle)

        # Dirt sprite
        self.dirt_wall = pygame.transform.rotate(pygame.image.load('game_files/sprites/tiles/dirt_floor.png'), angle)
        self.rect = self.dirt_wall.get_rect(topleft=init_pos)
