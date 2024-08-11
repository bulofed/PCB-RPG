from src.gui.gui_element import GUIElement
from src.utils.imports import pygame

class Button(GUIElement):
    def __init__(self, size: tuple, position: tuple=(0,0), text: str|None=None, font:pygame.font.Font|None=None, image:str|None=None, text_color: tuple|None=None, hovered_image: str|None=None, hovered_text_color: tuple|None=None, anchor: list=['top','left'], parent=None, layer: int=1):
        super().__init__(size, position, anchor, parent, layer)
        self.text = text
        self.image = image
        self.font = font
        self.text_color = text_color
        self.hovered_image = hovered_image
        self.hovered_text_color = hovered_text_color
        self.hovered = False
        self.create_image()
        
    def create_image(self):
        if self.image:
            self.image = pygame.image.load(self.image).convert_alpha()
            self.image = pygame.transform.scale(self.image, self.size)
        if self.text:
            self.text_surface = self.font.render(self.text, True, self.text_color)
            self.text_rect = self.text_surface.get_rect(center=self.rect.center)
            
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        if self.text:
            screen.blit(self.text_surface, self.text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hovered = True
            else:
                self.hovered = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
    
    def update(self, screen):
        if self.hovered:
            if self.hovered_image:
                self.image = pygame.image.load(self.hovered_image).convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size)
            if self.hovered_text_color:
                self.text_surface = self.font.render(self.text, True, self.hovered_text_color)
        else:
            if self.image:
                self.image = pygame.image.load(self.image).convert_alpha()
                self.image = pygame.transform.scale(self.image, self.size)
            if self.text:
                self.text_surface = self.font.render(self.text, True, self.text_color)
        self.draw(screen)