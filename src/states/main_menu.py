from src.utils.imports import pygame_gui, pygame, sys
from src.states.game_state import GameState

class MainMenu(GameState):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def set_gui(self):
        
        screen_width = self.screen.get_width()
        
        container_rect = pygame.Rect((0, 0), (screen_width - 100, 50))
        container_rect.bottom = -20
        
        container = pygame_gui.core.UIContainer(
            relative_rect=container_rect,
            manager=self.gui_manager,
            anchors={'bottom': 'bottom', 'centerx': 'centerx'}
        )
        
        self.start_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            text='Start Game',
            manager=self.gui_manager,
            container=container
        )
        
        quit_btn_rect = pygame.Rect((0, 0), (200, 50))
        quit_btn_rect.right = 0
        
        self.quit_btn = pygame_gui.elements.UIButton(
            relative_rect=quit_btn_rect,
            text='Quit',
            manager=self.gui_manager,
            container=container,
            anchors={'right': 'right'}
        )
        
        self.options_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            text='Options',
            manager=self.gui_manager,
            container=container,
            anchors={'centerx': 'centerx'}
        )
        
        self.gui_elements.extend([self.start_btn, self.quit_btn, self.options_btn])
    
    def run(self):
        self.screen.fill((155, 155, 155))
       
    def handle_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_btn:
                self.game_state_manager.set_state = 'sprite maker'
            elif event.ui_element == self.quit_btn:
                pygame.quit()
                sys.exit()
            elif event.ui_element == self.options_btn:
                self.game_state_manager.set_state = 'options'