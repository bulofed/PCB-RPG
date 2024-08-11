from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = []

    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def handle_events(self, event):
        pass