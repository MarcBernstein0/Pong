from typing import List, Tuple
import pygame

class Paddle(pygame.sprite.Sprite):
    screen: pygame.Surface
    color: pygame.Color
    position: List[int] # x, y
    dimensions: Tuple[int, int] # Width, Height
    width: int # if the paddle is filled or not
    up_key: int
    down_key: int

    def __init__(self, screen: pygame.Surface, up_key: int, down_key: int, color: pygame.Color, position: list[int], grps: pygame.sprite.Group, dimensions: Tuple[int, int] = (20, 90), width: int = 0) -> None:
        super().__init__(grps)
        self.screen = screen
        self.color = color
        self.position = position
        self.dimensions = dimensions
        self.width = width
        self.up_key = up_key
        self.down_key = down_key

    def __str__(self) -> str:
        res = self.__class__.__name__ + '(' + \
            ', '.join('%s=%s' % item for item in vars(self).items()) + ')'
        return res

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, (self.position[0], self.position[1], self.dimensions[0], self.dimensions[1]))


    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[self.up_key]:
            self.__move_up()
        if pressed[self.down_key]:
            self.__move_down()

    def __move_up(self):
        if (not self.__hit_ceiling()):
            self.position[1] -= 1
    
    def __move_down(self):
        if (not self.__hit_floor()):
            self.position[1] += 1

    def __hit_ceiling(self) -> bool:
        return self.position[1] <= 0

    def __hit_floor(self) -> bool:
        _, height = self.screen.get_size()
        return self.position[1] >= height - self.dimensions[1]
    