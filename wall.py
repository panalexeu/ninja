import pygame


class Wall:

    def __init__(self, surface, init_pos, angle):
        # Dirt sprite
        self.dirt_wall = pygame.transform.rotate(pygame.image.load('game_files/sprites/tiles/dirt_wall.png'), angle)
        self.rect = self.dirt_wall.get_rect(topleft=init_pos)

        # Surface on which will be displayed the object
        self.surface = surface

    def render(self):
        self.surface.blit(self.dirt_wall, (self.rect.x, self.rect.y))
