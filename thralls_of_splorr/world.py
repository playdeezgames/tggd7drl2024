import random
from pick_up import PickUp
import grimoire
import item_types


class World:
    def __init__(self):
        self.left_wall = 0
        self.right_wall = grimoire.BOARD_COLUMNS - 1
        self.position = (grimoire.BOARD_COLUMNS // 2, grimoire.BOARD_ROWS // 2)
        self.pick_ups = [[self.generate_left_wall(), self.generate_right_wall()] for _ in range(0, grimoire.BOARD_ROWS)]
        self.direction = 0
        self.pick_up_generator = {
            item_types.COPPER: 1,
            item_types.NOTHING: 9
        }

    def generate_left_wall(self):
        return PickUp(self.left_wall, item_types.DEATH)

    def generate_right_wall(self):
        return PickUp(self.right_wall, item_types.DEATH)

    def generate_pick_up(self):
        position = random.randrange(self.left_wall + 1, self.right_wall - 1)
        my_item_type = random.choices(list(self.pick_up_generator.keys()), list(self.pick_up_generator.values()))
        return PickUp(position, my_item_type[0])

    def set_direction(self, direction):
        self.direction = direction

    def advance(self):
        self.position = (self.position[0] + self.direction, self.position[1])
        self.pick_ups.pop(0)
        self.pick_ups.append([self.generate_left_wall(), self.generate_right_wall(), self.generate_pick_up()])

