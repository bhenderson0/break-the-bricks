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
    def __init__(self, bx, by, colour, number, row, col, health=1):
        super().__init__(bx, by, colour, number, row, col, health)
        pygame.gfxdraw.filled_circle(
                self.image,
                constants.B_WIDTH // 2,
                constants.B_HEIGHT // 2,
                constants.B_HEIGHT // 3,
                constants.BOMB_COLOUR)

    def explode(self, rows, cols, bricks_to_add):
        if self.row - 1 >= 0:
            bricks_to_add.add((self.row - 1) * cols + self.col)
        if self.row + 1 <= rows:
            bricks_to_add.add((self.row + 1) * cols + self.col)
        if self.col - 1 >= 0:
            bricks_to_add.add(self.row * cols + (self.col - 1))
        if self.col + 1 <= cols:
            bricks_to_add.add(self.row * cols + (self.col + 1))


class LargeBombBrick(Brick):
    def __init__(self, bx, by, colour, number, row, col, health=1):
        super().__init__(bx, by, colour, number, row, col, health)
        pygame.gfxdraw.filled_circle(
                self.image,
                constants.B_WIDTH // 2,
                constants.B_HEIGHT // 2,
                constants.B_HEIGHT // 2,
                constants.BOMB_COLOUR)

    def explode(self, rows, cols, bricks_to_add):
        if self.row - 2 >= 0:
            bricks_to_add.add((self.row - 2) * cols + self.col)
        if self.row + 2 <= rows:
            bricks_to_add.add((self.row + 2) * cols + self.col)
        if self.col - 2 >= 0:
            bricks_to_add.add(self.row * cols + (self.col - 2))
        if self.col + 2 <= cols:
            bricks_to_add.add(self.row * cols + (self.col + 2))
        for row in range(self.row - 1, self.row + 2):
            for col in range(self.col - 1, self.col + 2):
                curr_num = row * cols + col
                if 0 <= row < rows and 0 <= col < cols and curr_num:
                    bricks_to_add.add(curr_num)
