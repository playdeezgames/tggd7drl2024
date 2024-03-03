class TitleState:
    def __init__(self, my_context):
        self.context = my_context

    def handle_event(self, event):
        pass

    def draw(self):
        self.context.write_text_xy((0, 0), "Thralls of SPLORR!!", 15)
