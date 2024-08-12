from src.utils.imports import pygame, os, pygame_gui
from src.constants.const import GAME_NAME, MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT, FPS
from src.managers.player_manager import PlayerManager
from src.managers.event_manager import EventManager
from src.managers.game_state_manager import GameStateManager
from src.states.main_menu import MainMenu
from src.states.game import Game

class Loop:
    def __init__(self):
        self.init_pygame()
        self.init_states()
        self.player_manager = PlayerManager()
        self.event_manager = EventManager(self)
        
    def init_pygame(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        self.screen = pygame.display.set_mode((MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.clock = pygame.time.Clock()
        self.running: bool = True
        self.fullscreen: bool = False
        self.mouse_pos = pygame.mouse.get_pos()
        self.gui_manager = pygame_gui.UIManager((MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT))
        
    def init_states(self):
        self.game_state_manager = GameStateManager('main_menu', self.running, self.gui_manager)
        mainMenu = MainMenu(self.screen, self.game_state_manager, self.gui_manager)
        game = Game(self.screen, self.game_state_manager, self.gui_manager)
        self.states = {
            'main_menu': mainMenu,
            'game': game
        }
        self.game_state_manager.states = self.states
        
    def run(self):
        self.player_manager.load_player()
        while self.running:
            time_delta = self.clock.tick(FPS) / 1000.0
            self.mouse_pos = pygame.mouse.get_pos()
            self.event_manager.manage_events() 
            self.states[self.game_state_manager.get_state].run()  
            self.gui_manager.update(time_delta)
            self.gui_manager.draw_ui(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)