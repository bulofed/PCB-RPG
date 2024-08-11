class StateManager:
    def __init__(self, loop):
        self.loop = loop

    def manage_states(self):
        self.loop.states[self.loop.game_state_manager.get_state].run()