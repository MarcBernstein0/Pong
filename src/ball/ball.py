from typing import Any, List, Tuple
import pygame

from src.paddle.paddle import Paddle


class Ball(pygame.sprite.Sprite):
    screen: pygame.Surface
    color: pygame.Color
    position: List[int]
    radius: int
    speed: List[int]

    def __init__(self, screen: pygame.Surface, position: List[int], color: pygame.Color, radius: int, speed: List[int] = [1,1]):
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
    
    def update(self, paddle_l: Paddle, paddle_r: Paddle):
        self.circle.move_ip(self.speed)
        width, height = self.screen.get_size()
        if self.circle.left <= 0 or self.circle.right >= width or self.circle.colliderect(paddle_l.rect) or self.circle.colliderect(paddle_r.rect):
            self.speed[0] *= -1
        if self.circle.top <= 0 or self.circle.bottom >= height:
            self.speed[1] *= -1
