import pygame

import grimoire
import tileset


class Assets:
    def __init__(self):
        self.images = [
            pygame.image.load("assets/images/romfont24x24_0.png").convert(),
            pygame.image.load("assets/images/romfont24x24_1.png").convert(),
            pygame.image.load("assets/images/romfont24x24_2.png").convert(),
            pygame.image.load("assets/images/romfont24x24_3.png").convert(),
            pygame.image.load("assets/images/romfont24x24_4.png").convert(),
            pygame.image.load("assets/images/romfont24x24_5.png").convert(),
            pygame.image.load("assets/images/romfont24x24_6.png").convert(),
            pygame.image.load("assets/images/romfont24x24_7.png").convert(),
            pygame.image.load("assets/images/romfont24x24_8.png").convert(),
            pygame.image.load("assets/images/romfont24x24_9.png").convert(),
            pygame.image.load("assets/images/romfont24x24_10.png").convert(),
            pygame.image.load("assets/images/romfont24x24_11.png").convert(),
            pygame.image.load("assets/images/romfont24x24_12.png").convert(),
            pygame.image.load("assets/images/romfont24x24_13.png").convert(),
            pygame.image.load("assets/images/romfont24x24_14.png").convert(),
            pygame.image.load("assets/images/romfont24x24_15.png").convert(),
        ]
        self.tilesets = [
            tileset.TileSet(
                image,
                grimoire.CELL_SIZE,
                (grimoire.TILE_COLUMNS, grimoire.TILE_ROWS)
            )
            for image in self.images
        ]

    def blit_tile(self, target, destination, tileset_index, tile_index):
        self.tilesets[tileset_index].tiles[tile_index].blit(target, destination)
