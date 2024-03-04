import grimoire
import pygame


class TitleState:
    def __init__(self, my_context):
        self.context = my_context

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.context.start_game()
                return grimoire.STATE_IN_PLAY
        return grimoire.STATE_TITLE

    def draw(self):
        self.context.write_text_xy_centered(grimoire.CELL_ROWS // 2, "Thralls of SPLORR!!", 15)
