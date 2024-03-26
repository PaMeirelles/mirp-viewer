import pygame
from constants import WHITE, BLACK, RADIUS, BORDER_RATIO, WIDTH, HEIGHT, DISTANCE_INSTANCE_1
import numpy as np
from sklearn.manifold import MDS


class Port:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.circle(win, BLACK, (self.x, self.y), RADIUS, 0)
        pygame.draw.circle(win, WHITE, (self.x, self.y), RADIUS * BORDER_RATIO, 0)


def bound_coordinates(coordinates, min_width, max_width, min_height, max_height):
    min_x, min_y = np.min(coordinates, axis=0)
    max_x, max_y = np.max(coordinates, axis=0)

    # Calculate scaling factors for width and height
    scale_x = (max_width - min_width) / (max_x - min_x)
    scale_y = (max_height - min_height) / (max_y - min_y)

    # Apply scaling and translation to fit within the bounds
    scaled_coordinates = (coordinates - [min_x, min_y]) * [scale_x, scale_y]

    # Translate scaled coordinates to fit within the specified bounds
    bounded_coordinates = scaled_coordinates + [min_width, min_height]

    return bounded_coordinates


def get_coords(distances, min_x, max_x, min_y, max_y):
    mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
    raw_coordinates = mds.fit_transform(distances)
    coordinates = bound_coordinates(raw_coordinates, min_x, max_x, min_y, max_y)
    print("Coordinates:")
    print(coordinates)
    return coordinates


def get_ports(distances):
    coords = get_coords(distances, RADIUS, WIDTH - RADIUS, RADIUS, HEIGHT - RADIUS)
    return [Port(port[0], port[1]) for port in coords]


if __name__ == '__main__':
    get_coords(DISTANCE_INSTANCE_1, RADIUS, WIDTH - RADIUS, RADIUS, HEIGHT - RADIUS)


