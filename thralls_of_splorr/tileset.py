import pygame

import tile


class TileSet:
    def __init__(self, image, cell_size, grid_size):
        self.tiles = []
        for grid_y in range(grid_size[1]):
            for grid_x in range(grid_size[0]):
                source_x = grid_x * cell_size[0]
                source_y = grid_y * cell_size[1]
                source_rect = pygame.Rect(source_x, source_y, cell_size[0], cell_size[1])
                self.tiles.append(tile.Tile(image, source_rect))
