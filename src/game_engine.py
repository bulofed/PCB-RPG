from src.utils.imports import pygame, pygame_gui
from src.constants.const import GAME_NAME, MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT, FPS
from src.managers.player_manager import PlayerManager
from src.managers.event_manager import EventManager
from src.managers.game_state_manager import GameStateManager

class GameEngine:
    """
    The GameEngine class is responsible for initializing the game, managing the game states,
    and running the main game loop.
    """
    
    def __init__(self) -> None:
        """
        Initialize the GameEngine class by setting up Pygame, game states, and managers.
        """
        self._init_pygame()
        self.game_state_manager = GameStateManager(self.screen, self.gui_manager)
        self.player_manager = PlayerManager()
        self.event_manager = EventManager(self.screen, self.fullscreen, self.game_state_manager, self.gui_manager)
        
    def _init_pygame(self) -> None:
        """
        Initialize Pygame and set up the display, clock, and GUI manager.
        """
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        self.screen = pygame.display.set_mode((MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.previous_windowed_screen_size = self.screen.get_size()
        self.clock = pygame.time.Clock()
        self.fullscreen: bool = False
        self.mouse_pos = pygame.mouse.get_pos()
        self.gui_manager = pygame_gui.UIManager((MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT), "src/themes/button.json")
        
    def run(self) -> None:
        """
        Run the main game loop, handling events, updating states, and rendering the screen.
        """
        self.player_manager.load_player()
        while True:
            time_delta = self.clock.tick(FPS) / 1000.0
            self.mouse_pos = pygame.mouse.get_pos()
            self.event_manager.manage_events() 
            self.game_state_manager.active_state.run()
            self.gui_manager.update(time_delta)
            self.gui_manager.draw_ui(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)