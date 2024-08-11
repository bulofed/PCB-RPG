from src.utils.imports import os


####################################
#                                  #
#              PyGame              #
#                                  #
####################################


FPS = 60
MIN_SCREEN_WIDTH = 1280
MIN_SCREEN_HEIGHT = 720
GAME_NAME = "PCB MMORPG"
BG = (0, 0, 0)


####################################
#                                  #
#               Data               #
#                                  #
####################################


DATA_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data") # src/data
os.makedirs(DATA_FOLDER, exist_ok=True) # Create the data folder if it doesn't exist
SAVE_PATH = os.path.join(DATA_FOLDER, "player_save.pkl")