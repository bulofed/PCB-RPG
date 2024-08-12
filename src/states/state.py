from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, display, gameStateManager, gui_manager) -> None:
        self.display = display
        self.game_state_manager = gameStateManager
        self.gui_manager = gui_manager
        self.gui_elements = []
        self.set_gui()

    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def handle_events(self, event):
        pass
    
    @abstractmethod
    def set_gui(self):
        pass
    
    def hide_gui(self):
        for element in self.gui_elements:
            element.visible = 0

    def show_gui(self):
        for element in self.gui_elements:
            element.visible = 1