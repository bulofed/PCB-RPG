from src.gui.gui_element import GUIElement

class GUIGroup(GUIElement):
    def __init__(self, position: tuple, size: tuple, anchor: list=['top','left'], parent=None, layer: int=1):
        super().__init__(position, size, None, anchor, parent, layer)
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def draw(self, screen):
        for element in self.elements:
            element.draw(screen)

    def handle_event(self, event):
        for element in self.elements:
            element.handle_event(event)