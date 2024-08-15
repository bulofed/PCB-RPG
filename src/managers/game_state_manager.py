from typing import Dict
from src.states.main_menu import MainMenu
from src.states.options import Options
from src.states.sprite_maker import SpriteMaker
from src.states.game_state import GameState
from src.utils.imports import pygame, pygame_gui

class GameStateManager:
    def __init__(self, screen: pygame.Surface, gui_manager: pygame_gui.UIManager) -> None:
        self.states: Dict[str, GameState] = {
            'main menu': MainMenu(screen, gui_manager, self),
            'options': Options(screen, gui_manager, self),
            'sprite maker': SpriteMaker(screen, gui_manager, self)
        }
        self.active_state: GameState = self.states['main menu']
    
    @property
    def get_state(self) -> GameState:
        return self.active_state
    
    @get_state.setter
    def set_state(self, state: str) -> None:
        self.active_state.hide_gui()
        self.active_state = self.states[state]
        self.active_state.show_gui()