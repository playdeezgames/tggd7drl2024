import grimoire
import world
import item_types
import messages


class Context:
    def __init__(self, assets, target):
        self.assets = assets
        self.target = target
        self.world = None

    def get_world(self):
        return self.world

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

    def write_text_xy_centered(self, y, text, color, columns=grimoire.CELL_COLUMNS):
        self.write_text_xy(((columns - len(text)) // 2, y), text, color)

    def start_game(self):
        self.world = world.World()
        messages.clear()

    def draw_board(self, xy):
        x = self.world.position[0] - 1
        y = self.world.position[1] + 1
        w = 3
        while y < grimoire.BOARD_ROWS:
            for n in range(w):
                self.write_text_xy((x + n, y), "\xdb", 8)
            self.write_text_xy((x, y), "/", 0)
            self.write_text_xy((x + w - 1, y), "\\", 0)
            self.write_text_xy((x + w // 2, y), "|", 0)
            x -= 1
            y += 1
            w += 2
        for y in range(0, grimoire.BOARD_ROWS):
            for pick_up in self.world.pick_ups[y]:
                if pick_up is not None:
                    my_item_type = item_types.TABLE[pick_up.item_type]
                    self.write_text_xy((pick_up.position, y), my_item_type.text, my_item_type.color)
        if self.world.game_over:
            self.write_text_xy((xy[0] + self.world.position[0], xy[1] + self.world.position[1]), "\x01", 4)
        else:
            self.write_text_xy((xy[0] + self.world.position[0], xy[1] + self.world.position[1]), "\x02", 15)

    def set_direction(self, direction):
        self.world.direction = direction

    def advance(self):
        self.world.advance()
