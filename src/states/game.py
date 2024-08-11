from src.utils.imports import pygame
from src.states.state import State

class Game(State):
    def __init__(self, display, gameStateManager, font) -> None:
        super().__init__(display, gameStateManager)
        self.font = font
    
    def run(self):
        self.display.fill((0, 0, 0))
        
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.gameStateManager.set_state = 'main_menu'
    