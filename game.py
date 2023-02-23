import pygame

import settings
import level
import ninja
import hp_bar
import energy_bar

class Game:

    def __init__(self, scale_factor):
        pygame.init()

        # Screen and surface for screen scaling init
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.surface = pygame.Surface((settings.SURF_WIDTH, settings.SURF_HEIGHT), pygame.SRCALPHA)

        # Clock for working with ticks and fps
        self.clock = pygame.time.Clock()

        # Scale factor
        self.scale_factor = scale_factor

        # Level init passing to it level surface to blit on it game objects
        self.level = level.Level(self.surface)

        # Ninja init
        self.ninja = ninja.Ninja(self.surface, (-8, -8))  # (-8, -8) left corner coordinates for the sprite centre

        # UI inits (hp bar, energy bar)
        self.hp_bar = hp_bar.HpBar(self.surface, (1, 0))
        self.energy_bar = energy_bar.EnergyBar(self.surface, (1, 9 * self.scale_factor))

    def run(self):
        while True:
            # Scaling surface on the screen size
            self.screen.blit(pygame.transform.scale(self.surface, (settings.WIDTH, settings.HEIGHT)), (0, 0))

            self.surface.fill((100, 100, 100))

            # Level rendering
            # self.level.render()

            # Ninja rendering
            self.ninja.render()

            # UI renders (hp bar, energy bar)
            self.hp_bar.render(self.ninja.get_hp(), self.scale_factor)
            self.energy_bar.render(self.ninja.get_energy(), self.scale_factor)

            pygame.display.update()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()

                if event.type == pygame.QUIT:
                    quit()
