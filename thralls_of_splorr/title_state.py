import grimoire


class TitleState:
    def __init__(self, my_context):
        self.context = my_context

    def handle_event(self, event):
        pass

    def draw(self):
        self.context.write_text_xy_centered(grimoire.CELL_ROWS // 2, "Thralls of SPLORR!!", 15)
