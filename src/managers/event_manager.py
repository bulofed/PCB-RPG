from src.utils.imports import pygame

class EventManager:
    def __init__(self, loop):
        self.loop = loop

    def manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handle_quit_event()
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown_event(event)
            self.handle_other_events(event)

    def handle_quit_event(self):
        self.loop.running = False

    def handle_keydown_event(self, event):
        if event.key == pygame.K_F11:
            self.toggle_fullscreen()

    def toggle_fullscreen(self):
        self.loop.fullscreen = not self.loop.fullscreen
        if self.loop.fullscreen:
            self.loop.screen = pygame.display.set_mode(self.loop.MONITOR_SIZE, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
        else:
            self.loop.screen = pygame.display.set_mode(self.loop.screen_size, pygame.DOUBLEBUF | pygame.HWSURFACE)

    def handle_other_events(self, event):
        self.loop.states[self.loop.game_state_manager.get_state].handle_events(event)
        self.loop.gui_manager.process_events(event)