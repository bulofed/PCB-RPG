from src.utils.imports import pygame, sys

class EventManager:
    def __init__(self, screen, fullscreen, game_state_manager, gui_manager):
        self.screen = screen
        self.fullscreen = fullscreen
        self.game_state_manager = game_state_manager
        self.gui_manager = gui_manager

    def manage_events(self):
        active_state = self.game_state_manager.get_state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            active_state.handle_events(event)
            self.gui_manager.process_events(event)