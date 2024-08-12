class GameStateManager:
    def __init__(self, currentState, running, gui_manager) -> None:
        self.currentState = currentState
        self.running = running
        self.gui_manager = gui_manager
    
    @property
    def get_state(self):
        return self.currentState
    
    @get_state.setter
    def set_state(self, state):
        if self.currentState in self.states:
            self.states[self.currentState].hide_gui()
        self.currentState = state
        if self.currentState in self.states:
            self.states[self.currentState].show_gui()
        
    def quit(self):
        self.running = False