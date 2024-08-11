class GameStateManager:
    def __init__(self, currentState) -> None:
        self.currentState = currentState
    
    @property
    def get_state(self):
        return self.currentState
    
    @get_state.setter
    def set_state(self, state):
        self.currentState = state