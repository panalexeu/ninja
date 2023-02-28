import pygame


class Box:

    def __init__(self, surface, init_pos):
        # Box sprite
        self.box_sprite = pygame.image.load('game_files/sprites/object/box.png')
        self.box_rect = self.box_sprite.get_rect(topleft=init_pos)

        # Destroyed box sprite
        self.no_box = pygame.image.load('game_files/sprites/object/no_box.png')

        # Surface on which will be displayed the object
        self.surface = surface

    def box_collide(self, obj):
        if obj.colliderect(self.box_rect):
            return True

    def render(self):
        self.surface.blit(self.box_sprite, (self.box_rect.x, self.box_rect.y))