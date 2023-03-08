import pygame
import sys
from pygame.locals import QUIT

import constants
from levels.levels import LevelGenerator
from game_objects.ball import Ball
from game_objects.player import Player

pygame.init()
vec = pygame.math.Vector2

fps = pygame.time.Clock()
display = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Break the Bricks")

player = Player()
ball = Ball()
paddle_sprites = pygame.sprite.Group()
paddle_sprites.add(player)
ball_sprites = pygame.sprite.Group()
ball_sprites.add(ball)
brick_sprites = pygame.sprite.Group()
level_generator = LevelGenerator(brick_sprites)


def display_text(display, text_to_display, colour, size, location):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text_to_display, True, colour)
    text_rect = text.get_rect()
    text_rect.center = location
    display.blit(text, text_rect)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display.fill((0, 0, 0))
    level_generator.generate_level()

    level_text = f'Level: {level_generator.get_current_level()}'
    location = (constants.WIDTH // 2, 20)
    display_text(display, level_text, constants.WHITE, 32, location)

    pygame.sprite.Group.draw(brick_sprites, display)
    pygame.sprite.Group.draw(paddle_sprites, display)
    pygame.sprite.Group.draw(ball_sprites, display)

    player.move()
    ball.move(vec((player.pos.x, player.pos.y)))

    if pygame.sprite.collide_rect(player, ball):
        ball.collide_with_paddle(player)

    bricks_hit = pygame.sprite.spritecollide(ball, brick_sprites, False)
    if bricks_hit:
        ball.collide_with_brick(bricks_hit[0])
    for brick in bricks_hit:
        if (brick.damage() < 1):
            brick_sprites.remove(brick)

    pygame.display.update()
    fps.tick(constants.FPS)

