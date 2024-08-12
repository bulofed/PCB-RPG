from src.utils.imports import pygame
from src.states.state import State

class Game(State):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
    def set_gui(self):
        pass
    
    def run(self):
        self.display.fill((0, 0, 0))
        
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game_state_manager.set_state = 'main_menu'
    