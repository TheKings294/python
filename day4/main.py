import pygame
import sys
from Map import *

WIDTH, HEIGHT = 960, 960

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")

clock = pygame.time.Clock()

tileSet = TileSet('assets/tiles.png')
tileMap = TileMap(tileSet)

image = pygame.image.load('assets/tiles.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill((0, 0, 0))

    screen.blit(image, (0, 0))

    pygame.display.flip()
    clock.tick(60)