import pickle

class Player:
    def __init__(self, player_name, player_class):
        self.player_name = player_name
        self.player_class = player_class

    def __str__(self):
        return f"{self.player_name}'s class: {self.player_class}"
    
    def save(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
            
    @staticmethod
    def load(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)