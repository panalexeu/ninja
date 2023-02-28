import random

import pygame

import box
import dummy
import hp_pickup
import energy_pickup


class Level:
    test = pygame.image.load('game_files/sprites/tile/test.png')

    def __init__(self, surface):
        self.surface = surface

        # Objects list
        self.objects = []

        # Enemies list
        self.enemies = []

        # Pickups
        self.pickups = []

        # Box init
        self.level_box = box.Box(self.surface, (16*5, 16*5))
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
        self.objects.append(self.level_box)
        self.objects.append(self.level_box2)
        self.objects.append(self.level_box3)
        self.objects.append(self.level_box4)
        self.objects.append(self.level_box5)
        self.objects.append(self.level_box6)
        self.objects.append(self.level_box1)
        self.objects.append(self.level_box7)
        self.objects.append(self.level_box8)
        self.objects.append(self.level_box9)
        self.objects.append(self.level_box10)
        self.objects.append(self.level_box11)


        # Enemy init
        self.dummy = dummy.Dummy(self.surface, (16 * 10, 16 * 5))
        self.dummy1 = dummy.Dummy(self.surface, (16 * 13, 16 * 5))
        self.dummy2 = dummy.Dummy(self.surface, (16 * 16, 16 * 5))
        self.dummy3 = dummy.Dummy(self.surface, (16 * 19, 16 * 5))
        self.dummy4 = dummy.Dummy(self.surface, (16 * 22, 16 * 5))
        self.dummy5 = dummy.Dummy(self.surface, (16 * 25, 16 * 5))
        self.dummy6 = dummy.Dummy(self.surface, (16 * 9, 16 * 4))
        self.dummy7 = dummy.Dummy(self.surface, (16 * 1, 16 * 7))
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
        self.enemies.append(self.dummy7)
        self.enemies.append(self.dummy8)
        self.enemies.append(self.dummy9)

        # Pickups init
        self.pickups_init()

    def pickups_init(self):
        for box_obj in self.objects:
            # Temporary decision
            choice = random.randint(0, 1)
            print(choice)

            if choice == 0:
                self.pickups.append(hp_pickup.HpPickup(self.surface, (box_obj.box_rect.x, box_obj.box_rect.y)))
            if choice == 1:
                self.pickups.append(energy_pickup.EnergyPickup(self.surface, (box_obj.box_rect.x, box_obj.box_rect.y)))

    # Level objects collisions with projectiles
    def obj_proj_collision(self, projectiles):
        for obj in self.objects:
            for proj in projectiles:
                if obj.box_collide(proj.proj_rect):
                    self.objects.remove(obj)
                    projectiles.remove(proj)

    #  Level enemies collisions with projectiles
    def enemy_proj_collision(self, projectiles):
        for enemy in self.enemies:
            for proj in projectiles:
                if enemy.dummy_rect.colliderect(proj.proj_rect):
                    enemy.dmg_registration(proj.dmg)
                    projectiles.remove(proj)

    def back_render(self):
        self.surface.blit(self.test, (6 * 16, 8 * 16))

    def pickups_render(self):
        for pickup in self.pickups:
            pickup.render()

    def obj_render(self):
        for level_object in self.objects:
            level_object.render()

    def enemy_render(self):
        for enemy in self.enemies:
            enemy.render()
