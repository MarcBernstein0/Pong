from typing import Tuple
import pygame

from src.fps.fps import FPS
from src.paddle.paddle import Paddle

PADDLE_SPACING = 20
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1080


def makeScreen(backgroundColor: pygame.Color, caption: str) -> pygame.Surface:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(caption) 
    screen.fill(backgroundColor)
    pygame.display.flip() 
    return screen



def main():
    pygame.init()
    fps = FPS()
    screen_color = pygame.Color("black")
    screen = makeScreen(screen_color, "PONG")
    sprites = pygame.sprite.Group()
    paddle_left = Paddle(screen, pygame.K_w, pygame.K_s, pygame.Color("white"), [PADDLE_SPACING, SCREEN_HEIGHT//2], sprites)
    paddle_right = Paddle(screen, pygame.K_UP, pygame.K_DOWN, pygame.Color("white"),[SCREEN_WIDTH - (PADDLE_SPACING + 20), int(SCREEN_HEIGHT//1.5)], sprites)
  
    # Variable to keep our game loop running 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                running = False

        screen.fill(screen_color) # Clear the screen
        fps.clock.tick(180)
        fps.render(screen)
        sprites.update()
        paddle_left.draw_paddle()
        paddle_right.draw_paddle()


        pygame.display.update()

    print("Quitting game")


if __name__ == "__main__":
    main()