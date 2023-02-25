import pygame

import constants

vec = pygame.math.Vector2


class Brick(pygame.sprite.Sprite):
    """
    The bricks that the player needs to hit with the ball
    """

    def __init__(self, bx, by, colour, health=1):
        super().__init__()
        self.image = pygame.Surface((constants.B_WIDTH, constants.B_HEIGHT))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.pos = vec((bx, by))
        self.rect.midbottom = (bx, by)
        self.health = health

    def damage(self, amount=1):
        self.health -= amount
        return self.health
