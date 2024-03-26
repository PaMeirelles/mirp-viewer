import pygame
from constants import WHITE, BLACK, RADIUS, BORDER_RATIO


class Port:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.circle(win, BLACK, (self.x, self.y), RADIUS, 0)
        pygame.draw.circle(win, WHITE, (self.x, self.y), RADIUS * BORDER_RATIO, 0)
