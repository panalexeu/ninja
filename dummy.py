import pygame

import draw_text
import colors


class Dummy:

    def __init__(self, surface, init_pos):
        # Stats
        self.hp = 90

        # Dmg registration variables
        self.dmg_reg_text = ''
        self.dmg_reg = False
        self.dmg_reg_cooldown = 500
        self.dmg_reg_time = None

        # Surface on which will be displayed the object
        self.surface = surface

        # Sprites
        self.dummy = pygame.image.load('game_files/sprites/enemy/dummy/dummy.png')
        self.dummy_rect = self.dummy.get_rect(topleft=init_pos)

        self.no_dummy = pygame.image.load('game_files/sprites/enemy/dummy/no_dummy.png')

    def dmg_registration(self, dmg):
        self.dmg_reg = True
        self.hp -= dmg
        self.dmg_reg_text = str(dmg)
        self.dmg_reg_time = pygame.time.get_ticks()

    def death_check(self):
        if self.hp <= 0:
            self.hp = 0
            self.dummy = self.no_dummy

    def cooldown(self):
        current_time = pygame.time.get_ticks()

        if self.dmg_reg:
            if current_time - self.dmg_reg_cooldown >= self.dmg_reg_time:
                self.dmg_reg_text = ''
                self.dmg_reg = False

    def render(self):
        self.surface.blit(self.dummy, (self.dummy_rect.x, self.dummy_rect.y))
        self.cooldown()
        self.death_check()

        # Hp render
        self.surface.blit(draw_text.text(str(self.hp), 'prstart.ttf', 5, colors.RED),
                          (self.dummy_rect.topleft[0] - 11, self.dummy_rect.topleft[1]))

        # Dmg register render
        self.surface.blit(draw_text.text(self.dmg_reg_text, 'prstart.ttf', 5, colors.BLACK),
                          (self.dummy_rect.topright))