DEATH = "death"
COPPER = "copper"
NOTHING = "nothing"


class ItemType:
    def __init__(self, text, color):
        self.text = text
        self.color = color


TABLE = {
    NOTHING: ItemType(" ", 0),
    DEATH: ItemType("\xea", 8),
    COPPER: ItemType("\x9b", 6),
}
