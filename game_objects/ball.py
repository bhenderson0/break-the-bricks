import math
import pygame
import pygame.gfxdraw
from pygame.locals import K_DOWN

import constants

vec = pygame.math.Vector2


class Ball(pygame.sprite.Sprite):
    """
    The ball that bounces around to hit the bricks
    """

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((17, 17), pygame.SRCALPHA)
        pygame.gfxdraw.filled_circle(self.image, 8, 8, 8, constants.BALL_COLOUR)
        self.rect = self.image.get_rect()
        self.pos = vec((constants.WIDTH // 2, 20))
        self.vel = vec(0, constants.BALL_SPEED)
        self.acc = vec(0, 0)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        # For development purposes
        if pressed_keys[K_DOWN]:
            self.pos = vec((constants.WIDTH // 2, constants.HEIGHT // 2))
            self.vel = vec(0, constants.BALL_SPEED)

        self.pos += self.vel
        self.rect.midbottom = self.pos

        if self.pos.y > constants.HEIGHT:
            self.pos.y = 0
            self.vel = vec(0, constants.BALL_SPEED)

        elif self.pos.y < 8:
            self.vel = vec(self.vel.x, -self.vel.y)

        elif self.pos.x < 8 or self.pos.x > constants.WIDTH - 8:
            self.vel = vec(-self.vel.x, self.vel.y)

    def collide_with_paddle(self, paddle):
        pos_diff = self.pos.x - paddle.pos.x
        if math.fabs(pos_diff) < 5:
            self.vel = vec(0, -constants.BALL_SPEED)
        else:
            self.vel = vec(pos_diff / constants.BOUNCE, -constants.BALL_SPEED)

