import pygame
from constants import BLACK, VESSEL_RADIUS, BORDER_RATIO


class Vessel:
    def __init__(self, color, speed, x, y):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, BLACK, (self.x, self.y), VESSEL_RADIUS, 0)
        pygame.draw.circle(win, self.color, (self.x, self.y), VESSEL_RADIUS * BORDER_RATIO, 0)

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

