from src.states.state import State
from src.gui.button import Button
from src.utils.imports import pygame, sys

class MainMenu(State):
    def __init__(self, display, gameStateManager, font) -> None:
        super().__init__(display, gameStateManager)
        self.font = font
        self.create_buttons()
    
    def create_buttons(self):
        
        start_game_button = Button(
            size=(200, 50),
            text="Start Game",
            font=self.font,
            text_color=(0, 0, 0),
            hovered_text_color=(255, 255, 255),
            anchor=['center'],
        )
        
        self.buttons = [start_game_button]
    
    def run(self):
        self.display.fill((155, 155, 155))
        for button in self.buttons:
            button.update(self.display)
       
    def handle_events(self, event):
        for button in self.buttons:
            if button.handle_event(event):
                self.gameStateManager.set_state = 'game'
                break