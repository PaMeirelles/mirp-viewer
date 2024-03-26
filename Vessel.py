import pygame
from constants import BLACK, VESSEL_RADIUS, BORDER_RATIO, TERM_SPEED, TRAY_WIDTH, TRAY_TRANSPARENCY, WIDTH, HEIGHT



class Vessel:
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.speed = TERM_SPEED
        self.direction = [0, 0]
        self.color = color
        self.start = None
        self.target = None

    def draw(self, win):
        pygame.draw.circle(win, BLACK, (self.x, self.y), VESSEL_RADIUS, 0)
        pygame.draw.circle(win, self.color, (self.x, self.y), VESSEL_RADIUS * BORDER_RATIO, 0)
        if self.start and self.target:
            tray_color = self.color[:3] + (TRAY_TRANSPARENCY * 128,)
            tray_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.line(win, tray_color, self.start, (self.x, self.y), TRAY_WIDTH)
            pygame.draw.line(tray_surf, tray_color, self.target, (self.x, self.y), TRAY_WIDTH)
            win.blit(tray_surf, (0, 0))

    def move(self):
        if self.target:
            distance_to_target = ((self.target[0] - self.x) ** 2 + (self.target[1] - self.y) ** 2) ** 0.5

            distance_to_travel = self.speed

            if distance_to_target > distance_to_travel:
                self.x += self.direction[0] * self.speed
                self.y += self.direction[1] * self.speed
            else:
                self.start = None
                self.target = None

    def set_target(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y

        magnitude = (dx ** 2 + dy ** 2) ** 0.5

        if magnitude != 0:
            self.direction = (dx / magnitude, dy / magnitude)

        self.target = (target_x, target_y)
        self.start = (self.x, self.y)
