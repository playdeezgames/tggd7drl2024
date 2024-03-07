import random
from pick_up import PickUp
import grimoire
import item_types
import messages
import statistics


class World:
    def __init__(self):
        self.left_wall = 0
        self.right_wall = grimoire.BOARD_COLUMNS - 1
        self.position = (grimoire.BOARD_COLUMNS // 2, grimoire.BOARD_ROWS // 2)
        self.pick_ups = [[self.generate_left_wall(), self.generate_right_wall()] for _ in range(0, grimoire.BOARD_ROWS)]
        self.direction = 0
        self.inventory = {}
        self.pick_up_generator = {
            item_types.COPPER: 100,
            item_types.SILVER: 10,
            item_types.GOLD: 1,
            item_types.NOTHING: 900,
            item_types.ENERGY_BOOST: 100,
            item_types.HEALTH_BOOST: 10,
            item_types.ENERGY_DELTA_BUFF: 10,
            item_types.ENERGY_DELTA_DEBUFF: 100,
            item_types.ENERGY_STORE: 100,
            item_types.EXPERIENCE_BOOST: 10,
            item_types.MOVE_AHEAD: 10,
            item_types.MOVE_BACK: 5,
            item_types.QUEST_START: 5,
            item_types.QUEST_FINISH: 0,
            item_types.MACGUFFIN: 0,
        }
        self.game_over = False
        self.statistics = {}
        self.init_statistic(statistics.SCORE, 0, 0, None)
        self.init_statistic(statistics.HEALTH, 100, 0, 100)
        self.init_statistic(statistics.ENERGY, 100, 0, 100)
        self.init_statistic(statistics.ENERGY_DELTA, 25, 10, 50)
        self.init_statistic(statistics.EXPERIENCE, 0, 0, 10)
        self.init_statistic(statistics.EXPERIENCE_LEVEL, 1, 1, None)

    def change_generator_weight(self, item_type, delta):
        self.pick_up_generator[item_type] = max(0, self.pick_up_generator[item_type] + delta)

    def init_statistic(self, statistic, value, minimum, maximum):
        self.statistics[statistic] = (value, minimum, maximum)

    def set_statistic(self, statistic, value):
        minimum = self.get_statistic(statistic)[1]
        maximum = self.get_statistic(statistic)[2]
        if minimum is not None:
            value = max(minimum, value)
        if maximum is not None:
            value = min(maximum, value)
        self.statistics[statistic] = (value, minimum, maximum)

    def get_score(self):
        return self.get_statistic(statistics.SCORE)

    def get_experience(self):
        return self.get_statistic(statistics.EXPERIENCE)

    def get_experience_level(self):
        return self.get_statistic(statistics.EXPERIENCE_LEVEL)

    def get_health(self):
        return self.get_statistic(statistics.HEALTH)

    def get_energy(self):
        return self.get_statistic(statistics.ENERGY)

    def get_statistic(self, statistic):
        if statistic in self.statistics:
            return self.statistics[statistic]
        return None

    def change_statistic(self, statistic, delta):
        self.set_statistic(statistic, self.get_statistic(statistic)[0] + delta)

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

        self.change_statistic(statistics.SCORE, 1)
        if self.get_energy()[0] > 0:
            messages.write("-1 EN.", 3)
            self.change_statistic(statistics.ENERGY, -1)
        else:
            messages.write("-1 HP!", 4)
            self.change_statistic(statistics.HEALTH, -1)
            self.game_over = self.get_health()[0] <= 0
            if self.game_over:
                messages.write_line("", 0)
                messages.write_line("Starved to death!", 4)

        self.position = (self.position[0] + self.direction, self.position[1])
        self.pick_ups.pop(0)
        self.pick_ups.append(self.generate_pick_ups())
        self.process_pick_ups()
        messages.write_line("", 7)

    def generate_pick_ups(self):
        result = [self.generate_left_wall(), self.generate_right_wall(), self.generate_pick_up()]
        return result

    def process_pick_up(self, pick_up):
        if pick_up.item_type == item_types.ENERGY_STORE:
            energy = self.get_energy()
            spend = min(self.get_item_count(item_types.COPPER), energy[2] - energy[0])
            self.change_item_count(item_types.COPPER, -spend)
            self.change_statistic(statistics.ENERGY, spend)
            messages.write(f"-{spend}\x9b.", 6)
            messages.write(f"+{spend} EN.", 3)
        if pick_up.item_type == item_types.ENERGY_DELTA_DEBUFF:
            messages.write(f"-1 E\xeb.", 3)
            messages.write(f"+10 E%.", 3)
            self.change_statistic(statistics.ENERGY_DELTA, -1)
            self.change_generator_weight(item_types.ENERGY_BOOST, 10)
        elif pick_up.item_type == item_types.ENERGY_DELTA_BUFF:
            messages.write(f"+1 E\xeb.", 3)
            messages.write(f"+10 X%.", 4)
            self.change_statistic(statistics.ENERGY_DELTA, 1)
            self.change_generator_weight(item_types.NOTHING, 10)
        elif pick_up.item_type == item_types.COPPER:
            self.change_item_count(item_types.COPPER, 1)
            self.change_statistic(statistics.SCORE, 1)
            messages.write("+1\x9b!", 6)
        elif pick_up.item_type == item_types.SILVER:
            self.change_item_count(item_types.COPPER, 10)
            self.change_statistic(statistics.SCORE, 10)
            messages.write("+10\x9b!", 7)
        elif pick_up.item_type == item_types.GOLD:
            self.change_item_count(item_types.COPPER, 100)
            self.change_statistic(statistics.SCORE, 100)
            messages.write("+100\x9b!", 14)
        elif pick_up.item_type == item_types.DEATH:
            messages.write_line("", 0)
            messages.write_line("Instant death! GAME OVER!", 4)
            self.game_over = True
        elif pick_up.item_type == item_types.ENERGY_BOOST:
            energy_delta = self.get_statistic(statistics.ENERGY_DELTA)
            messages.write(f"+{energy_delta[0]} EN", 3)
            self.change_statistic(statistics.ENERGY, energy_delta[0])
            self.change_generator_weight(item_types.NOTHING, 1)
        elif pick_up.item_type == item_types.HEALTH_BOOST:
            messages.write("+10HP", 12)
            self.change_statistic(statistics.HEALTH, 10)
        elif pick_up.item_type == item_types.EXPERIENCE_BOOST:
            self.pick_up_experience_boost()
        elif pick_up.item_type == item_types.MOVE_BACK:
            self.pick_up_move_back()
        elif pick_up.item_type == item_types.MOVE_AHEAD:
            self.pick_up_move_ahead()
        elif pick_up.item_type == item_types.QUEST_START:
            self.pick_up_quest_start()
        elif pick_up.item_type == item_types.QUEST_FINISH:
            self.pick_up_quest_finish()
        elif pick_up.item_type == item_types.MACGUFFIN:
            self.pick_up_macguffin()

    def pick_up_quest_start(self):
        self.pick_up_generator[item_types.QUEST_START] = 0
        self.pick_up_generator[item_types.QUEST_FINISH] = 0
        self.pick_up_generator[item_types.MACGUFFIN] = 5
        messages.write("Quest Start!", 14)

    def pick_up_quest_finish(self):
        self.pick_up_generator[item_types.QUEST_START] = 5
        self.pick_up_generator[item_types.QUEST_FINISH] = 0
        self.pick_up_generator[item_types.MACGUFFIN] = 0
        messages.write("Quest Finish!", 14)
        self.pick_up_experience_boost(5)
        # Money?

    def pick_up_macguffin(self):
        self.pick_up_generator[item_types.QUEST_START] = 0
        self.pick_up_generator[item_types.QUEST_FINISH] = 10
        self.pick_up_generator[item_types.MACGUFFIN] = 0
        messages.write("Quest Item!", 14)

    def pick_up_move_back(self):
        if self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)

    def pick_up_move_ahead(self):
        if self.position[1] < grimoire.BOARD_COLUMNS - 1:
            self.position = (self.position[0], self.position[1] + 1)

    def pick_up_experience_boost(self, delta=1):
        self.change_statistic(statistics.EXPERIENCE, delta)
        messages.write(f"+{delta}XP.", 5)
        while self.get_experience()[0] >= self.get_experience()[2]:
            messages.write("+1LV.", 5)
            self.init_statistic(
                statistics.EXPERIENCE,
                self.get_experience()[0] - self.get_experience()[2],
                0,
                self.get_experience()[2] * 2)
            self.change_statistic(statistics.HEALTH, self.get_statistic(statistics.HEALTH)[2])
            self.change_statistic(statistics.ENERGY, self.get_statistic(statistics.ENERGY)[2])

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
