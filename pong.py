from typing import Tuple
import pygame


def makeScreen(backgroundColor: Tuple[int, int, int], caption: str) -> pygame.Surface:
    screen = pygame.display.set_mode((300, 300)) 
    pygame.display.set_caption(caption) 
    screen.fill(backgroundColor);
    pygame.display.flip() 
    return screen

def main():
    screen = makeScreen((234, 212, 252), "PONG")
    # Update the display using flip 
  
    # Variable to keep our game loop running 
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    print("Hello world")


if __name__ == "__main__":
    main()