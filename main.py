import pygame, sys
from pygame.locals import *
from const import *
from player import Player
from gamestatemanager import GameStateManager
from main_menu import MainMenu

class Game:
    def __init__(self):
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
        
        self.gameStateManager = GameStateManager('main_menu')
        self.mainMenu = MainMenu(self.screen, self.gameStateManager, self.font)
        
        self.states = {
            'main_menu': self.mainMenu
        }
        
        self.player = None
    
    def create_player(self):
        player_name = input("Enter player's name: ")
        player_class = input("Enter player's class: ")
        self.player = Player(player_name, player_class)
        self.player.save("player_save.pkl")
        print(self.player)
        
    def load_player(self):
        try:
            self.player = Player.load("player_save.pkl")
            print(self.player)
        except FileNotFoundError:
            print("No player found.")
            self.create_player()
        
    def manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode(self.MONITOR_SIZE, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
                    else:
                        self.screen = pygame.display.set_mode(self.screen_size, pygame.DOUBLEBUF | pygame.HWSURFACE)
                    self.mainMenu.update_buttons()
        
    def run(self):
        
        self.load_player()

        while self.running:
            
            self.mouse_pos = pygame.mouse.get_pos()
            
            self.manage_events()
            
            self.states[self.gameStateManager.get_state].run()
            
            for button in self.states[self.gameStateManager.get_state].buttons:
                button.changeColor(self.mouse_pos)
            
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ in "__main__":
    Game().run()
    pygame.quit()
    sys.exit()