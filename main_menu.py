from menu import Menu, Button

class MainMenu(Menu):
    def __init__(self, display, gameStateManager, font) -> None:
        super().__init__(display, gameStateManager, font)
        self.start_game_button = Button(None, (display.get_width() // 2, display.get_height() // 2), "Start Game", font, (0, 0, 0), (255, 255, 255))
        self.buttons.append(self.start_game_button)
    
    def run(self):
        self.display.fill((155, 155, 155))
        for button in self.buttons:
            button.update(self.display)