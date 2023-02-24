import pygame
import pygame.gfxdraw

import constants

vec = pygame.math.Vector2


class Ball(pygame.sprite.Sprite):
    """
    The ball that bounces around to hit the bricks
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((17, 17), pygame.SRCALPHA)
        pygame.gfxdraw.filled_circle(self.surf, 8, 8, 8, constants.BALL_COLOUR)
        self.rect = self.surf.get_rect()
        self.pos = vec((constants.WIDTH // 2, 20))
        self.vel = vec(0, constants.BALL_SPEED)

    def move(self):
        self.pos += self.vel

        self.rect.midbottom = self.pos

        if self.pos.y > constants.HEIGHT:
            self.pos.y = 0

    def collide_with_paddle(self, paddle):
        self.vel = (0, 0)
        print(self.pos, paddle.pos)

