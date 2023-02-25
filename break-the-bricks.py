import pygame
import sys
from pygame.locals import QUIT

import constants
from game_objects.ball import Ball
from game_objects.player import Player

pygame.init()
vec = pygame.math.Vector2

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

    pygame.sprite.Group.draw(main_sprites, display)

    player.move()
    ball.move()

    if pygame.sprite.collide_rect(player, ball):
        ball.collide_with_paddle(player)

    pygame.display.update()
    fps.tick(constants.FPS)

