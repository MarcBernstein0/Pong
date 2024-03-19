import pygame


COLOR = pygame.Color("chartreuse")

class FPS:
    clock: pygame.time.Clock
    font: pygame.font.SysFont
    text: pygame.Surface

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, COLOR)

    def render(self, display: pygame.Surface):
        self.text = self.font.render(str(round(self.clock.get_fps(),2)), True, COLOR)
        display.blit(self.text, (1000, 10))