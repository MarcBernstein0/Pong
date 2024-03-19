import pygame

class Paddle:
    screen: pygame.Surface
    color: tuple[int, int, int]
    position: tuple[int, int] # Left, Right
    dimensions: tuple[int, int] # Width, Height
    width: int # if the paddle is filled or not

    def __init__(self, screen: pygame.Surface, color: tuple[int, int, int], position: tuple[int, int] = (0,0), dimensions: tuple[int, int] = (500, 500), width: int = 0) -> None:
        self.screen = screen
        self.color = color
        self.position = position
        self.dimensions = dimensions
        self.width = width

    def __str__(self) -> str:
        attributes = dir(self)
        res = self.__class__.__name__ + '(' + \
            ', '.join('%s=%s' % item for item in vars(self).items()) + ')'
        return res