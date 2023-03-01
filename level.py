import random

import pygame

import map_file_init
import floor
import wall
import wall_corner
import box
import dummy
import hp_pickup
import energy_pickup


class Level:
    def __init__(self, surface):
        self.surface = surface

        # Level maps inits
        self.back_lvl_map = map_file_init.map_init('tutorial_lvl')

        # Objects list
        self.boxes = []
        self.wall_objects = []
        self.back_objects = []

        # Enemies list
        self.enemies = []

        # Pickups
        self.pickups = []

        self.level_box = box.Box(self.surface, (16 * 5, 16 * 5))
        self.level_box1 = box.Box(self.surface, (16 * 1, 16 * 2))
        self.level_box6 = box.Box(self.surface, (16 * 5, 16 * 2))
        self.level_box2 = box.Box(self.surface, (16 * 3, 16 * 4))
        self.level_box3 = box.Box(self.surface, (16 * 4, 16 * 4))
        self.level_box4 = box.Box(self.surface, (16 * 1, 16 * 5))
        self.level_box5 = box.Box(self.surface, (16 * 2, 16 * 4))
        self.level_box7 = box.Box(self.surface, (16 * 20, 16 * 12))
        self.level_box8 = box.Box(self.surface, (16 * 19, 16 * 12))
        self.level_box9 = box.Box(self.surface, (16 * 17, 16 * 12))
        self.level_box10 = box.Box(self.surface, (16 * 14, 16 * 12))
        self.level_box11 = box.Box(self.surface, (16 * 16, 16 * 12))

        # test append

        self.boxes.append(self.level_box7)
        self.boxes.append(self.level_box8)
        self.boxes.append(self.level_box9)
        self.boxes.append(self.level_box10)
        self.boxes.append(self.level_box11)

        # Enemy init
        self.dummy = dummy.Dummy(self.surface, (16 * 10, 16 * 5))
        self.dummy1 = dummy.Dummy(self.surface, (16 * 13, 16 * 5))
        self.dummy2 = dummy.Dummy(self.surface, (16 * 16, 16 * 5))
        self.dummy3 = dummy.Dummy(self.surface, (16 * 19, 16 * 5))
        self.dummy4 = dummy.Dummy(self.surface, (16 * 22, 16 * 5))
        self.dummy5 = dummy.Dummy(self.surface, (16 * 25, 16 * 5))
        self.dummy6 = dummy.Dummy(self.surface, (16 * 9, 16 * 4))
        self.dummy8 = dummy.Dummy(self.surface, (16 * 4, 16 * 8))
        self.dummy9 = dummy.Dummy(self.surface, (16 * 8, 16 * 9))

        # Enemy append
        self.enemies.append(self.dummy)
        self.enemies.append(self.dummy1)
        self.enemies.append(self.dummy2)
        self.enemies.append(self.dummy3)
        self.enemies.append(self.dummy4)
        self.enemies.append(self.dummy5)
        self.enemies.append(self.dummy6)
        self.enemies.append(self.dummy8)
        self.enemies.append(self.dummy9)

        # Level inits
        self.back_lvl_init()
        self.pickups_init()
        
    def pickups_init(self):
        for box_obj in self.boxes:
            # Temporary decision
            choice = random.randint(0, 1)
            print(choice)

            if choice == 0:
                self.pickups.append(hp_pickup.HpPickup(self.surface, (box_obj.rect.x, box_obj.rect.y)))
            if choice == 1:
                self.pickups.append(energy_pickup.EnergyPickup(self.surface, (box_obj.rect.x, box_obj.rect.y)))

    def back_lvl_init(self):

        y = 2
        for line in self.back_lvl_map:
            x = 2

            for column in line:

                if column == '0':
                    self.back_objects.append(floor.Floor(self.surface, (x*16, y*16), 0))

                if column == '1':
                    if y == 0+2:
                        tile_object = wall.Wall(self.surface, (x * 16, y * 16), 0)
                    if x == 0+2:
                        tile_object = wall.Wall(self.surface, (x * 16, y * 16), 90)
                    if y == 13+2:
                        tile_object = wall.Wall(self.surface, (x * 16, y * 16), 180)
                    if x == 25+2:
                        tile_object = wall.Wall(self.surface, (x * 16, y * 16), 270)

                if column == '2':
                    if x == 0+2 and y == 0+2:
                        tile_object = wall_corner.WallCorner(self.surface, (x * 16, y * 16), 0)
                    if x == 0+2 and y == 13+2:
                        tile_object = wall_corner.WallCorner(self.surface, (x * 16, y * 16), 90)
                    if x == 25+2 and y == 13+2:
                        tile_object = wall_corner.WallCorner(self.surface, (x * 16, y * 16), 180)
                    if x == 25+2 and y == 0+2:
                        tile_object = wall_corner.WallCorner(self.surface, (x * 16, y * 16), 270)

                self.wall_objects.append(tile_object)

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
        for obj in self.wall_objects:
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
        return self.wall_objects + self.boxes

    def back_render(self):
        for back_object in self.back_objects:
            back_object.render()

    def render(self):
        for wall_obj in self.wall_objects:
            wall_obj.render()

    def pickups_render(self):
        for pickup in self.pickups:
            pickup.render()

    def obj_render(self):
        for level_object in self.boxes:
            level_object.render()

    def enemy_render(self):
        for enemy in self.enemies:
            enemy.render()
