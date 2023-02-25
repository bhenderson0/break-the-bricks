import pygame
from pygame.locals import K_LEFT, K_RIGHT

import constants

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    """
    The paddle at the bottom of the screen
    """

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((76, 16))
        # self.image.fill((230, 0, 0))
        # self.image.fill((0, 100, 255, 155))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, constants.RED, (68, 8),  8)
        pygame.draw.circle(self.image, constants.RED, (8, 8),  8)
        pygame.draw.rect(
                self.image, constants.PADDLE_COLOUR, pygame.Rect(8, 0, 60, 16))
        self.pos = vec((constants.WIDTH // 2, constants.HEIGHT - 40))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def move(self):
        self.acc = vec(0, 0)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -constants.PLAYER_ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = constants.PLAYER_ACC

        self.acc.x += self.vel.x * constants.PLAYER_FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > constants.WIDTH:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = constants.WIDTH

        self.rect.midbottom = self.pos

