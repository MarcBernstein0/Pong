import pygame

class Paddle:
    screen: pygame.Surface
    color: pygame.Color
    position: list[int] # x, y
    dimensions: tuple[int, int] # Width, Height
    width: int # if the paddle is filled or not

    def __init__(self, screen: pygame.Surface, color: pygame.Color, position: list[int], dimensions: tuple[int, int] = (20, 90), width: int = 0) -> None:
        self.screen = screen
        self.color = color
        self.position = position
        self.dimensions = dimensions
        self.width = width

    def __str__(self) -> str:
        res = self.__class__.__name__ + '(' + \
            ', '.join('%s=%s' % item for item in vars(self).items()) + ')'
        return res

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, (self.position[0], self.position[1], self.dimensions[0], self.dimensions[1]))

    def move_up(self):
        self.position[1] -= 1
    
    def move_down(self):
        self.position[1] += 1

    