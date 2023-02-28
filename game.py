import pygame

import settings
import level
import ninja
import hp_bar
import energy_bar


class Game:

    def __init__(self, scale_factor):
        pygame.init()

        # Turning off the cursor
        pygame.mouse.set_visible(False)

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
            self.level.back_render()

            # Pickups level rendering
            self.level.pickups_render()

            # Ninja collisions test
            self.ninja.pickup_collision(self.level.pickups)

            # Ninja rendering
            self.ninja.render()

            # Object of the level render
            self.level.obj_render()

            # Enemy rendering
            self.level.enemy_render()

            # UI renders (hp bar, energy bar)
            self.hp_bar.render(self.ninja.hp, self.scale_factor)
            self.energy_bar.render(self.ninja.energy, self.scale_factor)

            # Level collisions test
            self.level.obj_proj_collision(self.ninja.projectiles)
            self.level.enemy_proj_collision(self.ninja.projectiles)

            pygame.display.update()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()

                if event.type == pygame.QUIT:
                    quit()
