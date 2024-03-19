from typing import Tuple
import pygame

from src.fps.fps import FPS
from src.paddle.paddle import Paddle


def makeScreen(backgroundColor: Tuple[int, int, int], caption: str) -> pygame.Surface:
    screen = pygame.display.set_mode((1080, 900))
    pygame.display.set_caption(caption) 
    screen.fill(backgroundColor)
    pygame.display.flip() 
    return screen



def main():
    pygame.init()
    fps = FPS()
    color = pygame.Color("black")
    screen = makeScreen(color, "PONG")
  
    # Variable to keep our game loop running 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        screen.fill(color)
 
        fps.clock.tick(180)
        fps.render(screen)
 
        pygame.display.update()

    print("Hello world")


if __name__ == "__main__":
    main()