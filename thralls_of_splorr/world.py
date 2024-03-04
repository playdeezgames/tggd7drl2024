import random
from pick_up import PickUp
import grimoire
import item_types
import messages


class World:
    def __init__(self):
        self.left_wall = 0
        self.right_wall = grimoire.BOARD_COLUMNS - 1
        self.position = (grimoire.BOARD_COLUMNS // 2, grimoire.BOARD_ROWS // 2)
        self.pick_ups = [[self.generate_left_wall(), self.generate_right_wall()] for _ in range(0, grimoire.BOARD_ROWS)]
        self.direction = 0
        self.inventory = {}
        self.pick_up_generator = {
            item_types.COPPER: 1,
            item_types.NOTHING: 9
        }
        self.game_over = False
        self.score = 0
        self.health = 100
        self.maximum_health = 100
        self.energy = 100
        self.maximum_energy = 100

    def generate_left_wall(self):
        return PickUp(self.left_wall, item_types.DEATH)

    def generate_right_wall(self):
        return PickUp(self.right_wall, item_types.DEATH)

    def generate_pick_up(self):
        position = random.randrange(self.left_wall + 1, self.right_wall - 1)
        my_item_type = random.choices(list(self.pick_up_generator.keys()), list(self.pick_up_generator.values()))
        return PickUp(position, my_item_type[0])

    def set_direction(self, direction):
        if self.game_over:
            return
        self.direction = direction

    def advance(self):
        if self.game_over:
            return
        if self.direction == -1:
            messages.write("Left!", 7)
        elif self.direction == 1:
            messages.write("Right!", 7)
        else:
            messages.write("Ahead!", 7)

        self.score += 1
        if self.energy > 0:
            messages.write("-1 EN.", 3)
            self.energy -= 1
        else:
            messages.write("-1 HP!", 4)
            self.health -= 1
            self.game_over = self.health <= 0
            if self.game_over:
                messages.write_line("", 0)
                messages.write_line("Starved to death!", 4)

        self.position = (self.position[0] + self.direction, self.position[1])
        self.pick_ups.pop(0)
        self.pick_ups.append([self.generate_left_wall(), self.generate_right_wall(), self.generate_pick_up()])
        self.process_pick_ups()
        messages.write_line("", 7)

    def process_pick_up(self, pick_up):
        if pick_up.item_type == item_types.COPPER:
            self.change_item_count(item_types.COPPER, 1)
            self.score += 1
            messages.write("+1\x9b!", 6)
        elif pick_up.item_type == item_types.DEATH:
            messages.write_line("", 0)
            messages.write_line("Instant death! GAME OVER!", 4)
            self.game_over = True

    def process_pick_ups(self):
        for pick_up in self.pick_ups[self.position[1]]:
            if pick_up.position == self.position[0]:
                self.process_pick_up(pick_up)
                pick_up.position = -1

    def get_item_count(self, item_type):
        if item_type not in self.inventory:
            return 0
        return self.inventory[item_type]

    def change_item_count(self, item_type, delta):
        if item_type not in self.inventory:
            self.inventory[item_type] = 0
        self.inventory[item_type] += delta
