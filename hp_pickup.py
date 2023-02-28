import pygame


class HpPickup:

    def __init__(self, surface, init_pos):
        # Stats
        self.hp_factor = 1

        # Hp pickup sprite
        self.pickup_sprite = pygame.image.load('game_files/sprites/pickup/hp/health.png')
        self.pickup_rect = self.pickup_sprite.get_rect(topleft=init_pos)

        # Surface on which will be displayed the object
        self.surface = surface

    def render(self):
        self.surface.blit(self.pickup_sprite, (self.pickup_rect.x, self.pickup_rect.y))
