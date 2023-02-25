import pygame
import sys
from pygame.locals import QUIT

import constants
from levels.levels import generate_level
from game_objects.ball import Ball
from game_objects.player import Player

pygame.init()
vec = pygame.math.Vector2

level_start = False
fps = pygame.time.Clock()
display = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Break the Bricks")

player = Player()
ball = Ball()
main_sprites = pygame.sprite.Group()
main_sprites.add(player, ball)
brick_sprites = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display.fill((0, 0, 0))

    if not level_start:
        level_start = True
        generate_level(brick_sprites, 1)

    pygame.sprite.Group.draw(brick_sprites, display)
    pygame.sprite.Group.draw(main_sprites, display)

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

