import pygame as pg
import sys
from const import *

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(GAME_NAME)
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.running: bool = True
        
    def run(self):

        while self.running:
            
            self.screen.fill(BG)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            
            pg.display.update()
            self.clock.tick(FPS)

if __name__ in "__main__":
    Game().run()
    pg.quit()
    sys.exit()