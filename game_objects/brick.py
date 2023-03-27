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

    def explode(self, rows, cols):
        pass

    def damage(self, amount=1):
        self.health -= amount
        return self.health


class BombBrick(Brick):
    def explode(self, rows, cols):
        bricks_to_add = []
        bricks_to_add.append((self.row + 1) * cols + self.col)  # below
        bricks_to_add.append((self.row - 1) * cols + self.col)  # above
        bricks_to_add.append(self.number - 1)  # before
        bricks_to_add.append(self.number + 1)  # after
        bricks_to_add = [
                brick for brick in bricks_to_add if 0 <= brick <= rows * cols]
        return bricks_to_add
