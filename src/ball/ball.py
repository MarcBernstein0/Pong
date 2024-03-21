from typing import Any, List, Tuple
import pygame


class Ball(pygame.sprite.Sprite):
    screen: pygame.Surface
    color: pygame.Color
    position: List[int]
    radius: int
    speed: List[int]

    def __init__(self, screen: pygame.Surface, position: List[int], color: pygame.Color, radius: int, *grps: pygame.sprite.Group, speed: List[int] = [1,1]):
        super().__init__(*grps)
        self.screen = screen
        self.position = position
        self.color = color
        self.radius = radius
        self.speed = speed
        self.circle = pygame.draw.circle(self.screen, self.color, self.position, self.radius)

    
    def __str__(self) -> str:
        res = self.__class__.__name__ + '(' + \
            ', '.join('%s=%s' % item for item in vars(self).items()) + ')'
        return res
    
    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, self.circle.center, self.radius)
    
    def update(self):
        self.circle.move_ip(self.speed)
        width, height = self.screen.get_size()
        if self.circle.left <= 0 or self.circle.right >= width:
            self.speed[0] *= -1
        if self.circle.top <= 0 or self.circle.bottom >= height:
            self.speed[1] *= -1
