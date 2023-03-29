from random import randint

import constants
from game_objects.brick import Brick, BombBrick, LargeBombBrick


def level_one(group):
    colours = [
            constants.YELLOW,
            constants.GREEN,
            constants.BLUE,
            constants.SALMON,
            constants.PURPLE
    ]
    num_rows = 5
    num_cols = 14
    for row in range(num_rows):
        for col in range(num_cols):
            brick_one = randint(0, 10)
            brick_two = randint(0, 50)
            # Todo: Improve how the bricks get created (remove these ugly ifs)
            if not brick_one:
                group.add(
                        BombBrick(
                            col * (constants.B_WIDTH + 2) + 30,
                            row * (constants.B_HEIGHT + 2) + 250,
                            constants.WHITE,
                            row * num_cols + col,
                            row,
                            col))
            elif not brick_two:
                group.add(
                        LargeBombBrick(
                            col * (constants.B_WIDTH + 2) + 30,
                            row * (constants.B_HEIGHT + 2) + 250,
                            constants.PADDLE_COLOUR,
                            row * num_cols + col,
                            row,
                            col))
            else:
                group.add(
                        Brick(
                            col * (constants.B_WIDTH + 2) + 30,
                            row * (constants.B_HEIGHT + 2) + 250,
                            colours[row],
                            row * num_cols + col,
                            row,
                            col))
    return (num_rows, num_cols)


def level_two(group):
    group.add(Brick(225, 200, constants.YELLOW))


class LevelGenerator:
    levels = [level_one, level_two]

    def __init__(self, group, start_level=1):
        self.level = start_level
        self.group = group
        self.start_of_level = True
        self.rows = 0
        self.cols = 0

    def generate_level(self):
        if self.start_of_level:
            self.rows, self.cols = self.levels[self.level - 1](self.group)
            self.start_of_level = False

    def increment_level(self):
        if self.level < len(self.levels):
            self.level += 1
            self.start_of_level = True

    def reset_to_beginning(self, start_level=1):
        self.level = start_level
        self.start_of_level = True

