import pygame
import sys

from Port import get_ports
from Vessel import Vessel
from constants import *
from random import choice

pygame.init()

screen_width = WIDTH
screen_height = HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MIRP Viewer")

clock = pygame.time.Clock()
is_running = True

ports = get_ports(DISTANCE_INSTANCE_1)
vessel = Vessel(RED, 2,[1, 0], 500, 500)

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    if vessel.target is None:
        target_port = choice(ports)
        vessel.set_target(target_port.x, target_port.y)

    vessel.move()

    screen.fill(WHITE)
    for p in ports:
        p.draw(screen)
    vessel.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
