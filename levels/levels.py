import constants
from game_objects.brick import Brick


def level_one(group):
    colours = [
            constants.YELLOW,
            constants.GREEN,
            constants.BLUE,
            constants.SALMON,
            constants.PURPLE
    ]
    for row in range(5):
        for col in range(14):
            group.add(
                    Brick(
                        col * (constants.B_WIDTH + 2) + 30,
                        row * (constants.B_HEIGHT + 2) + 250,
                        colours[row]))


def level_two(group):
    group.add(Brick(225, 200, constants.YELLOW))


class LevelGenerator:
    levels = [level_one, level_two]

    def __init__(self, group, start_level=1):
        self.level = start_level
        self.group = group
        self.start_of_level = True

    def generate_level(self):
        if self.start_of_level:
            self.levels[self.level - 1](self.group)
            self.start_of_level = False

    def increment_level(self):
        if self.level < len(self.levels):
            self.level += 1
            self.start_of_level = True

    def reset_to_beginning(self, start_level=1):
        self.level = start_level
        self.start_of_level = True

