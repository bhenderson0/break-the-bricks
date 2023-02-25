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


levels = [level_one, level_two]


def generate_level(group, level=1):
    levels[level - 1](group)

