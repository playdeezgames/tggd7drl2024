import grimoire


class Context:
    def __init__(self, assets, target):
        self.assets = assets
        self.target = target

    def write_text_xy(self, xy, text, color):
        for character in text:
            self.assets.blit_tile(
                self.target,
                (
                    xy[0] * grimoire.CELL_WIDTH,
                    xy[1] * grimoire.CELL_HEIGHT
                ),
                color,
                ord(character)
            )
            xy = (xy[0] + 1, xy[1])
