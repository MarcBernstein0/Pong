from typing import Any, List, Tuple
import pygame


class Ball(pygame.sprite.Sprite):
    screen: pygame.Surface
    color: pygame.Color
    position: List[int]
    radius: int
    vel_x: int
    vel_y: int

    def __init__(self, screen: pygame.Surface, position: List[int], color: pygame.Color, radius: int, vel_x: int, vel_y: int, *grps: pygame.sprite.Group):
        super().__init__(*grps)
        self.screen = screen
        self.position = position
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color
        self.radius = radius
    
    def __str__(self) -> str:
        res = self.__class__.__name__ + '(' + \
            ', '.join('%s=%s' % item for item in vars(self).items()) + ')'
        return res
    
    def draw_ball(self):
        print(self.position)
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)
    
    def update(self):
        height, width = self.screen.get_size()
        if (self.position[1] == 0 or self.position[1] == height):
            self.vel_x *= -1
        if (self.position[0] == 0 or self.position[0] == width):
            self.vel_y *= -1
        self.position[0] += self.vel_x
        self.position[1] += self.vel_y