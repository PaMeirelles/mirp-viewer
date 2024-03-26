import pygame
import sys

from Port import get_ports
from Vessel import Vessel
from constants import *
from random import choice
from Mirp import Mirp

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MIRP Viewer")

clock = pygame.time.Clock()
is_running = True

mirp = Mirp(DISTANCE_INSTANCE_7, STARTS_INSTANCE_1)

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    mirp.step()

    screen.fill(WHITE)
    mirp.draw(screen)

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
sys.exit()
