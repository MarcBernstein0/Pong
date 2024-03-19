from typing import Tuple
import pygame

from src.fps.fps import FPS
from src.paddle.paddle import Paddle


def makeScreen(backgroundColor: pygame.Color, caption: str) -> pygame.Surface:
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
    paddle = Paddle(screen, pygame.Color("white"), [20, 900//2])
  
    # Variable to keep our game loop running 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            if keys[pygame.K_w]:
                print("w key pressed")
                paddle.move_up()
            if keys[pygame.K_s]:
                print("s key pressed")
                paddle.move_down()

        screen.fill(color) # Clear the screen
        fps.clock.tick(180)
        fps.render(screen)
        paddle.draw_paddle()

 
        pygame.display.update()

    print("Quitting game")


if __name__ == "__main__":
    main()