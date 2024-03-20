from typing import List, Tuple
import pygame


class Ball(pygame.sprite.Sprite):
    screen: pygame.Surface
    color: pygame.Color
    position: List[int]
    radius: int

    def __init__(self, screen: pygame.Surface, position: List[int], color: pygame.Color, radius: int, *grps: pygame.sprite.Group):
        super().__init__(*grps)
        self.screen = screen
        self.position = position
        self.color = color
        self.radius = radius
    
    def __str__(self) -> str:
        res = self.__class__.__name__ + '(' + \
            ', '.join('%s=%s' % item for item in vars(self).items()) + ')'
        return res
    
    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)