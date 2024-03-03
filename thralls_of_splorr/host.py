import pygame

import context
import grimoire
import assets
import title_state


class Host:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(grimoire.SCREEN_SIZE)
        pygame.display.set_caption("Thralls of SPLORR!!")
        self.clock = pygame.time.Clock()
        self.assets = assets.Assets()
        self.context = context.Context(self.assets, self.screen)
        self.states = {
            grimoire.STATE_TITLE: title_state.TitleState(self.context),
        }
        self.current_state = grimoire.STATE_TITLE

    def get_current_state(self):
        return self.states[self.current_state]

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            else:
                self.get_current_state().handle_event(event)
        return True

    def __draw(self):
        self.screen.fill("black")
        self.get_current_state().draw()
        pygame.display.flip()
        self.clock.tick(grimoire.FPS)

    def run(self):
        while self.__handle_events():
            self.__draw()
        pygame.quit()
