import pygame


class Ninja:
    def __init__(self, surface, init_pos):
        # Stats
        self.hp = 3
        self.energy = 3
        self.speed = 3
        self.roll_factor = 1  # roll factor

        self.surface = surface

        self.frame = pygame.image.load('game_files/sprites/ghost/idle/idle_0.png')
        self.rect = self.frame.get_rect(topleft = init_pos)

        self.direction = pygame.math.Vector2()

        self.anim_buffer = []

        self.shd_factor = 12  # shadow factor (temporary decision)

        # Energy cooldown variables
        self.energy_loss = False
        self.energy_cooldown = 5000
        self.energy_time = None

        # Movement
        # Roll cooldown variables
        self.roll = False
        self.roll_cooldown = 1000
        self.roll_time = None

    def animation(self, action, frame_count, anim_len):
        for index in range(frame_count):
            for _ in range(anim_len):
                self.anim_buffer.append(f'game_files/sprites/ghost/{action}/{action}_{index}.png')
            index += 1

    def input(self):
        # Getting pressed keys
        keys = pygame.key.get_pressed()

        # Idle animation
        self.animation('idle', 1, 1)

        # y-axis moving
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.animation('mov_up', 1, 1)
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # x-axis moving
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.animation('mov_r', 1, 1)
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.animation('mov_l', 1, 1)
        else:
            self.direction.x = 0

        # Roll moving
        if keys[pygame.K_SPACE] and not self.roll:
            if self.energy > 0:
                self.roll = True
                self.roll_time = pygame.time.get_ticks()
                self.roll_factor = 2

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



    def get_hp(self):
        return self.hp

    def get_energy(self):
        return self.energy

    def render(self):
        self.input()
        self.cooldown()
        self.move()
