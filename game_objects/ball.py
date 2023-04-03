import math
import pygame
from pygame.locals import K_UP, K_DOWN

import constants

vec = pygame.math.Vector2


class Ball(pygame.sprite.Sprite):
    """
    The ball that bounces around to hit the bricks
    """

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((17, 17), pygame.SRCALPHA)
        pygame.gfxdraw.filled_circle(
                self.image, 8, 8, 8, constants.BALL_COLOUR)
        self.rect = self.image.get_rect()
        self.pos = vec((constants.WIDTH // 2, 20))
        self.vel = vec(0, constants.BALL_SPEED)
        self.acc = vec(0, 0)
        self.released = False
        self.number = 3
        self.cooldown = 500
        self.last = pygame.time.get_ticks()

    def move(self, player_pos):
        now = pygame.time.get_ticks()
        pressed_keys = pygame.key.get_pressed()

        if not self.released and pressed_keys[K_UP]:
            self.released = True
            self.vel.y = -constants.BALL_SPEED

        if pressed_keys[K_DOWN] and now - self.last >= self.cooldown:
            self.last = now
            self.released = False
            self.number -= 1

        if self.released:
            self.pos += self.vel

            if self.pos.y > constants.HEIGHT:
                self.released = False
                self.number -= 1

            elif self.pos.y < 8:
                self.vel = vec(self.vel.x, -self.vel.y)

            elif self.pos.x < 8 or self.pos.x > constants.WIDTH - 8:
                while self.pos.x < 8:
                    self.pos.x += 1
                while self.pos.x > constants.WIDTH - 8:
                    self.pos.x -= 1
                self.vel = vec(-self.vel.x, self.vel.y)

        else:
            self.pos = vec((player_pos.x, player_pos.y - 15))

        self.rect.midbottom = self.pos

    def collide_with_paddle(self, paddle):
        pos_diff = self.pos.x - paddle.pos.x
        if math.fabs(pos_diff) < 4:
            self.vel = vec(0, -constants.BALL_SPEED)
        else:
            self.vel = vec(pos_diff / constants.BOUNCE, -constants.BALL_SPEED)

    def collide_with_brick(self, brick):
        # Hit Top or bottom
        new_vy = -self.vel.y
        new_vx = self.vel.x
        # Hit one of the sides
        if abs(self.pos.y - brick.pos.y) < constants.B_HEIGHT / 2:
            new_vx = -self.vel.x
            new_vy = self.vel.y
        self.vel = vec(new_vx, new_vy)

