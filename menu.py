from abc import ABC, abstractmethod
from button import Button

class Menu(ABC):
    def __init__(self, display, gameStateManager, font):
        self.display = display
        self.gameStateManager = gameStateManager
        self.font = font
        self.buttons = []

    @abstractmethod
    def run(self):
        pass

    def update_buttons(self):
        for button in self.buttons:
            button.update_position((self.display.get_width() // 2, self.display.get_height() // 2))