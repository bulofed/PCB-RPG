from abc import ABC, abstractmethod
from typing import Optional
from src.utils.imports import pygame

class GUIElement(ABC):
    def __init__(self, size: tuple, position: tuple=(0,0), anchor: list=['top','left'], parent: Optional['GUIElement'] = None, layer: int=1):
        self.size = size
        self.position = position
        self.anchor = anchor
        self.parent = parent
        self.layer = layer
        self.rect = pygame.Rect(position, size)
        self.update_position()

    def update_position(self):
        if self.parent is None:
            screen_width, screen_height = pygame.display.get_surface().get_size()
            x, y = 0, 0

            if 'top' in self.anchor:
                y = self.position[1]
            elif 'bottom' in self.anchor:
                y = screen_height - self.position[1] - self.size[1]

            if 'left' in self.anchor:
                x = self.position[0]
            elif 'right' in self.anchor:
                x = screen_width - self.position[0] - self.size[0]
                
            if 'center' in self.anchor:
                x = (screen_width - self.size[0]) // 2
                y = (screen_height - self.size[1]) // 2
                
            if 'center_x' in self.anchor:
                x = (screen_width - self.size[0]) // 2
                
            if 'center_y' in self.anchor:
                y = (screen_height - self.size[1]) // 2
                
            x += self.position[0]
            y += self.position[1]

            self.rect.topleft = (x, y)
        else:
            self.rect.topleft = self.position

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass