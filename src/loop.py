from src.utils.imports import pygame, os
from src.constants.const import GAME_NAME, MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT, FPS
from src.managers.player_manager import PlayerManager
from src.managers.event_manager import EventManager
from src.managers.state_manager import StateManager
from src.managers.game_state_manager import GameStateManager
from src.states.main_menu import MainMenu
from src.states.game import Game

class Loop:
    def __init__(self):
        self.init_pygame()
        self.init_states()
        self.player_manager = PlayerManager()
        self.event_manager = EventManager(self)
        self.state_manager = StateManager(self)
        
    def init_pygame(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        self.MONITOR_SIZE = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.screen = pygame.display.set_mode((MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.clock = pygame.time.Clock()
        self.running: bool = True
        self.fullscreen: bool = False
        self.screen_size = self.screen.get_size()
        self.font = pygame.font.Font(None, 36)
        self.mouse_pos = pygame.mouse.get_pos()
        
    def init_states(self):
        self.game_state_manager = GameStateManager('main_menu')
        mainMenu = MainMenu(self.screen, self.game_state_manager, self.font)
        game = Game(self.screen, self.game_state_manager, self.font)
        self.states = {
            'main_menu': mainMenu,
            'game': game
        }
        
    def run(self):
        self.player_manager.load_player()
        while self.running:
            self.mouse_pos = pygame.mouse.get_pos()
            self.event_manager.manage_events()   
            self.state_manager.manage_states()
            pygame.display.update()
            self.clock.tick(FPS)