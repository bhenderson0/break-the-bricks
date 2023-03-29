import pygame

import constants

vec = pygame.math.Vector2


class Brick(pygame.sprite.Sprite):
    """
    The bricks that the player needs to hit with the ball
    """

    def __init__(self, bx, by, colour, number, row, col, health=1):
        super().__init__()
        self.image = pygame.Surface((constants.B_WIDTH, constants.B_HEIGHT))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.pos = vec((bx, by))
        self.rect.midbottom = (bx, by)
        self.health = health
        self.number = number
        self.row = row
        self.col = col

    def explode(self, rows, cols, bricks_to_add):
        pass

    def damage(self, amount=1):
        self.health -= amount
        return self.health


class BombBrick(Brick):
    def explode(self, rows, cols, bricks_to_add):
        for row in range(self.row - 1, self.row + 2):
            for col in range(self.col - 1, self.col + 2):
                curr_num = row * cols + col
                if 0 <= row < rows and 0 <= col < cols and curr_num:
                    bricks_to_add.add(curr_num)
