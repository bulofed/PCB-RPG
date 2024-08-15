from abc import ABC, abstractmethod
from typing import List
from src.utils.imports import pygame, pygame_gui

class GameState(ABC):
    def __init__(self, screen: pygame.Surface, gui_manager: pygame_gui.UIManager, game_state_manager) -> None:
        self.screen: pygame.Surface = screen
        self.gui_manager: pygame_gui.UIManager = gui_manager
        self.game_state_manager = game_state_manager
        self.gui_elements: List[pygame_gui.elements.UIElement] = []
        self.set_gui()

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def handle_events(self, event: pygame.event.Event) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def set_gui(self) -> None:
        raise NotImplementedError
    
    def hide_gui(self) -> None:
        for element in self.gui_elements:
            element.visible = 0

    def show_gui(self) -> None:
        for element in self.gui_elements:
            element.visible = 1