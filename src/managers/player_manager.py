from src.models.player import Player
from src.constants.const import SAVE_PATH

class PlayerManager:
    def __init__(self):
        self.player = None

    def create_player(self):
        player_name = input("Enter player's name: ")
        player_class = input("Enter player's class: ")
        self.player = Player(player_name, player_class)
        self.player.save(SAVE_PATH)
        print(self.player)

    def load_player(self):
        try:
            self.player = Player.load(SAVE_PATH)
            print(self.player)
        except FileNotFoundError:
            print("No player found.")
            self.create_player()