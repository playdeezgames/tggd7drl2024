import random

DEATH = "death"
COPPER = "copper"
SILVER = "silver"
GOLD = "gold"
NOTHING = "nothing"
ENERGY_BOOST = "energy boost"
HEALTH_BOOST = "health boost"
ENERGY_DELTA_BUFF = "energy delta buff"
ENERGY_DELTA_DEBUFF = "energy delta debuff"
ENERGY_STORE = "energy store"
EXPERIENCE_BOOST = "experience boost"
MOVE_BACK = "move back"
MOVE_AHEAD = "move ahead"
QUEST_START = "quest start"
QUEST_FINISH = "quest finish"
MACGUFFIN = "macguffin"


class ItemType:
    def __init__(self, text, color, counter=0, active=False):
        self.text = text
        self.color = color
        self.initial_counter = counter
        self.reset_value = counter
        self.counter = random.randrange(0, counter) if counter != 0 else 0
        self.active = active


TABLE = {
    NOTHING: ItemType(" ", 0, 0, False),
    DEATH: ItemType("\xea", 0, 0, False),
    COPPER: ItemType("\x9b", 6, 5, True),
    SILVER: ItemType("\x9b", 7, 50, True),
    GOLD: ItemType("\x9b", 14, 500, True),
    ENERGY_BOOST: ItemType("\x2b", 3, 15, True),
    ENERGY_DELTA_BUFF: ItemType("\x18", 3, 60, True),
    ENERGY_DELTA_DEBUFF: ItemType("\x19", 3, 60, True),
    HEALTH_BOOST: ItemType("\x2b", 12, 30, True),
    ENERGY_STORE: ItemType("$", 3, 30, True),
    EXPERIENCE_BOOST: ItemType("+", 5, 90, True),
    MOVE_BACK: ItemType("\x18", 15, 180, True),
    MOVE_AHEAD: ItemType("\x19", 15, 90, True),
    QUEST_START: ItemType("?", 14, 60, True),
    QUEST_FINISH: ItemType("!", 14, 0, False),
    MACGUFFIN: ItemType("\x9d", 14, 0, False),
}
