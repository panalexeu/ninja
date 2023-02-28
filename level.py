import random

import pygame

import map_file_init
import wall
import wall_corner
import box
import dummy
import hp_pickup
import energy_pickup


class Level:
    def __init__(self, surface):
        self.surface = surface

        # Playable surface
        self.play_surface = pygame.Surface((416, 224))

        # Level maps inits
        self.back_lvl_map = map_file_init.map_init('tutorial_lvl')

        # Level tiles loads
        self.dirt_wall = pygame.image.load('game_files/sprites/tiles/dirt_wall.png')
        self.dirt_corner = pygame.image.load('game_files/sprites/tiles/dirt_corner1.png')

        # Objects list
        self.boxes = []
        self.back_objects = []

        # Enemies list
        self.enemies = []

        # Pickups
        self.pickups = []

        # Level inits
        self.back_lvl_init()
        self.pickups_init()

    def pickups_init(self):
        for box_obj in self.boxes:
            # Temporary decision
            choice = random.randint(0, 1)
            print(choice)

            if choice == 0:
                self.pickups.append(hp_pickup.HpPickup(self.surface, (box_obj.box_rect.x, box_obj.box_rect.y)))
            if choice == 1:
                self.pickups.append(energy_pickup.EnergyPickup(self.surface, (box_obj.box_rect.x, box_obj.box_rect.y)))

    def back_lvl_init(self):
        y = 0
        for line in self.back_lvl_map:
            x = 0

            for column in line:
                if column == '1':
                    if y == 0:
                        tile_object = wall.Wall(self.play_surface, (x * 16, y * 16), 0)
                    if x == 0:
                        tile_object = wall.Wall(self.play_surface, (x * 16, y * 16), 90)
                    if y == 13:
                        tile_object = wall.Wall(self.play_surface, (x * 16, y * 16), 180)
                    if x == 25:
                        tile_object = wall.Wall(self.play_surface, (x * 16, y * 16), 270)

                if column == '2':
                    if x == 0 and y == 0:
                        tile_object = wall_corner.WallCorner(self.play_surface, (x * 16, y * 16), 0)
                    if x == 0 and y == 13:
                        tile_object = wall_corner.WallCorner(self.play_surface, (x * 16, y * 16), 90)
                    if x == 25 and y == 13:
                        tile_object = wall_corner.WallCorner(self.play_surface, (x * 16, y * 16), 180)
                    if x == 25 and y == 0:
                        tile_object = wall_corner.WallCorner(self.play_surface, (x * 16, y * 16), 270)

                self.back_objects.append(tile_object)

                x += 1
            y += 1

    # Level objects collisions with projectiles
    def obj_proj_collision(self, projectiles):
        for obj in self.boxes:
            for proj in projectiles:
                if obj.box_collide(proj.proj_rect):
                    self.boxes.remove(obj)
                    projectiles.remove(proj)

    # Level wall objects collisions with projectiles
    def wall_proj_collision(self, projectiles):
        for obj in self.back_objects:
            for proj in projectiles:
                if obj.rect.colliderect(proj.proj_rect):
                    projectiles.remove(proj)

    #  Level enemies collisions with projectiles
    def enemy_proj_collision(self, projectiles):
        for enemy in self.enemies:
            for proj in projectiles:
                if enemy.dummy_rect.colliderect(proj.proj_rect):
                    enemy.dmg_registration(proj.dmg)
                    projectiles.remove(proj)

    def collide_objects(self):
        return self.back_objects + self.boxes

    def render(self):
        self.play_surface.fill((43, 26, 13))

        for back_object in self.back_objects:
            back_object.render()

        self.surface.blit(self.play_surface, (32, 23))

    def pickups_render(self):
        for pickup in self.pickups:
            pickup.render()

    def obj_render(self):
        for level_object in self.boxes:
            level_object.render()

    def enemy_render(self):
        for enemy in self.enemies:
            enemy.render()
