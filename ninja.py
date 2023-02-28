import math

import pygame

import gun
import revolver
import hp_pickup
import energy_pickup

class Ninja:

    def __init__(self, surface, init_pos):
        # Stats
        self.hp = 3
        self.energy = 5
        self.speed = 3
        self.roll_factor = 1  # roll factor

        # Surface on which will be displayed the player
        self.surface = surface

        # Player image load
        self.frame = pygame.image.load('game_files/sprites/ghost/idle/idle_0.png')
        self.ghost_rect = self.frame.get_rect(topleft=init_pos)

        # Player cursor load
        self.cursor = pygame.image.load('game_files/sprites/mouse/cursor.png')
        # self.cursor_rect = self.cursor.get_rect()

        # Gun init
        self.gun = revolver.Revolver((self.ghost_rect.centerx, self.ghost_rect.centery), self.surface)

        # For gun rotation
        self.mx, self.my = 0, 0
        self.correction_angle = 0
        self.angle = 0

        # Direction Vector
        self.direction = pygame.math.Vector2()

        # Animation buffer
        self.anim_buffer = []

        # Projectiles list (which deletes a projectile with collision)
        self.projectiles = []

        # Energy cooldown variables
        self.energy_loss = False
        self.energy_cooldown = 5000
        self.energy_time = None

        # Shot cooldown variable
        self.shot = False
        self.shot_cooldown = self.gun.fire_rate
        self.shot_time = None

        # Movement
        # Roll cooldown variables
        self.roll = False
        self.roll_cooldown = 500
        self.roll_time = None

    # animations function
    def animation(self, action, frame_count, anim_len):
        for index in range(frame_count):
            for _ in range(anim_len):
                self.anim_buffer.append(f'game_files/sprites/ghost/{action}/{action}_{index}.png')
            index += 1

    def mouse_input(self):
        # Getting mouse input
        self.mx, self.my = pygame.mouse.get_pos()

        # Mouse calculations
        # + 12 value depends on gun size we use, temporary decision, should be reworked
        dx, dy = self.mx - self.ghost_rect.centerx + self.gun.x_factor, self.my - self.ghost_rect.centery + self.gun.y_factor
        self.angle = math.degrees((math.atan2(-dy, dx))) - self.correction_angle

    def key_input(self):
        # Getting pressed keys
        keys = pygame.key.get_pressed()

        # Idle animation
        self.animation('idle', 1, 1)

        # Check do we perform the roll if so input is blocked
        if not self.roll:
            # y-axis moving
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.animation('mov_up', 1, 1)
            elif keys[pygame.K_s]:
                self.direction.y = 1
            else:
                self.direction.y = 0

            # x-axis moving
            if keys[pygame.K_d]:
                self.direction.x = 1
                self.animation('mov_r', 1, 1)
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.animation('mov_l', 1, 1)
            else:
                self.direction.x = 0

        # Action is performed (shot)
        if keys[pygame.K_e] and not self.shot:
            # Gun recoil
            self.angle += self.gun.recoil

            # Shot cooldown
            self.shot = True
            self.shot_time = pygame.time.get_ticks()

            # Projectile initialization
            self.projectiles.append(self.gun.shot([self.gun.gun_rect.x, self.gun.gun_rect.y], [self.mx, self.my]))

        # Roll moving
        if keys[pygame.K_SPACE] and not self.roll:
            # If the player is moving we perform the roll
            if self.direction.x != 0 or self.direction.y != 0:
                # If we have energy
                if self.energy > 0:
                    # Roll factor enabled and variables for cooldown
                    self.roll = True
                    self.roll_time = pygame.time.get_ticks()
                    self.roll_factor = 2

                    # Energy decremented and variables for cooldown
                    self.energy_loss = True
                    self.energy_time = pygame.time.get_ticks()
                    self.energy -= 1

        # Roll animation handling
        if self.roll:
            if self.direction.y == -1 and self.direction.x == 0:
                self.animation('roll_up', 1, 1)
            else:
                self.animation('roll_dw', 1, 1)

    def move(self):
        # Movement handling
        self.ghost_rect.center += self.direction * self.speed * self.roll_factor

        # Ghost animation handling
        self.frame = pygame.image.load(self.anim_buffer.pop())

        # Ghost displaying
        self.surface.blit(self.frame, (self.ghost_rect.centerx, self.ghost_rect.centery))

        # Gun displaying
        self.gun.gun_pos(self.ghost_rect.centerx, self.ghost_rect.centery)
        self.surface.blit(pygame.transform.rotate(self.gun.gun_sprite, self.angle), (self.gun.gun_rect.x, self.gun.gun_rect.y))
        # pygame.draw.line(self.surface, (0, 0, 0), (self.ghost_rect.centerx + 12, self.ghost_rect.centery), (self.mx, self.my), 1)

        # Cursor displaying
        self.surface.blit(self.cursor, (self.mx, self.my))

    def cooldown(self):
        current_time = pygame.time.get_ticks()

        # Energy cooldown handling
        if self.energy_loss:
            if current_time - self.energy_time >= self.energy_cooldown:
                self.energy += 1
                self.energy_loss = False

        # Shot cooldown handling
        if self.shot:
            if current_time - self.shot_time >= self.shot_cooldown:
                self.shot = False

        # Roll cooldown handling
        if self.roll:
            if current_time - self.roll_time >= self.roll_cooldown:
                self.roll_factor = 1
                self.roll = False

    def pickup_collision(self, pickup_objects: list):
        for pickup_obj in pickup_objects:
            if self.ghost_rect.colliderect(pickup_obj.pickup_rect):
                if isinstance(pickup_obj, hp_pickup.HpPickup) and self.hp < 5:
                    self.hp += pickup_obj.hp_factor
                if isinstance(pickup_obj, energy_pickup.EnergyPickup) and self.energy < 5:
                    self.energy += pickup_obj.energy_factor
                pickup_objects.remove(pickup_obj)

    def ghost_projectiles(self):
        # Projectiles render and handling
        for projectile in self.projectiles:
            projectile.move()

    def render(self):
        self.mouse_input()
        self.key_input()
        self.cooldown()
        self.move()
        self.ghost_projectiles()
