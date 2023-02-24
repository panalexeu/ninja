import math

import pygame

import gun


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
        self.rect = self.frame.get_rect(topleft=init_pos)

        # Player cursor load
        self.cursor = pygame.image.load('game_files/sprites/test/cursor.png')
        self.cursor_rect = self.cursor.get_rect()

        # For gun rotation
        self.gun = gun.Gun()
        self.mx, self.my = 0, 0
        self.correction_angle = 0
        self.angle = 0

        # Direction Vector
        self.direction = pygame.math.Vector2()

        # Animation buffer
        self.anim_buffer = []

        # Projectiles list
        self.projectiles = []

        # Shadow factor
        self.shd_factor = 12  # shadow factor (temporary decision)

        # Energy cooldown variables
        self.energy_loss = False
        self.energy_cooldown = 5000
        self.energy_time = None

        # Movement
        # Roll cooldown variables
        self.roll = False
        self.roll_cooldown = 500
        self.roll_time = None

    def animation(self, action, frame_count, anim_len):
        for index in range(frame_count):
            for _ in range(anim_len):
                self.anim_buffer.append(f'game_files/sprites/ghost/{action}/{action}_{index}.png')
            index += 1

    def input(self):
        # Getting pressed keys
        keys = pygame.key.get_pressed()

        # Getting mouse input
        self.mx, self.my = pygame.mouse.get_pos()

        # Mouse calculations
        dx, dy = self.mx - self.rect.centerx + 12, self.my - self.rect.centery
        self.angle = math.degrees((math.atan2(-dy, dx))) - self.correction_angle

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
        if keys[pygame.K_e]:
            # Gun recoil
            self.angle += self.gun.recoil

            # Projectile initialization
            self.projectiles.append(self.gun.shot([self.rect.centerx, self.rect.centery], [self.mx, self.my], self.surface))

        # Roll moving
        if keys[pygame.K_SPACE] and not self.roll:
            # If we have energy
            if self.energy > 0:
                # Check did we had any directions before the space pressed if not we perform down roll
                if self.direction.x == 0 and self.direction.y == 0:
                    self.direction.y = 1

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
        self.rect.center += self.direction * self.speed * self.roll_factor

        # Shadow displaying
        # pygame.draw.ellipse(self.surface, (32, 32, 32),
        #                     (self.rect.center[0], self.rect.center[1] + self.shd_factor, 16, 8))

        # Ghost animation handling
        self.frame = pygame.image.load(self.anim_buffer.pop())

        # Ghost displaying
        self.surface.blit(self.frame, (self.rect.center[0], self.rect.center[1]))

        # Gun displaying
        # line
        # pygame.draw.line(self.surface, (0, 0, 0), (self.rect.centerx + 12, self.rect.centery), (self.mx, self.my), 1)
        self.surface.blit(pygame.transform.rotate(self.gun.gun_sprite, self.angle), (self.rect.center[0] + 12, self.rect.center[1] - 4))

        # Projectiles render
        for projectile in self.projectiles:
            projectile.move()

        # Cursor displaying
        self.surface.blit(self.cursor, (self.mx, self.my))

    def cooldown(self):
        current_time = pygame.time.get_ticks()

        # Energy cooldown handling
        if self.energy_loss:
            if current_time - self.energy_time >= self.energy_cooldown:
                self.energy += 1
                self.energy_loss = False

        # Roll cooldown handling
        if self.roll:
            if current_time - self.roll_time >= self.roll_cooldown:
                self.roll_factor = 1
                self.roll = False

    def render(self):
        self.input()
        self.cooldown()
        self.move()
