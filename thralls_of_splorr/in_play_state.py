import pygame

import grimoire


class InPlayState:
    def __init__(self, my_context):
        self.context = my_context

    def handle_key(self, key):
        if key == pygame.K_LEFT:
            self.context.set_direction(-1)
            self.context.advance()
        elif key == pygame.K_RIGHT:
            self.context.set_direction(1)
            self.context.advance()
        return grimoire.STATE_IN_PLAY

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            return self.handle_key(event.key)
        return grimoire.STATE_IN_PLAY

    def draw(self):
        self.context.draw_board((0, 0))
