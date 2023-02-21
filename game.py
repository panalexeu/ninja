import sys

import pygame

import settings
import level


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.surface = pygame.Surface((settings.SURF_WIDTH, settings.SURF_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = level.Level(self.surface)

    def run(self):
        while True:
            # Scaling surface on the screen size
            self.screen.blit(pygame.transform.scale(self.surface, (settings.WIDTH, settings.HEIGHT)), (0, 0))

            self.surface.fill((0, 0, 0))
            self.level.render()

            pygame.display.update()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
