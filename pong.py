import pygame

from src.game_logic.game_logic import GameLogic

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
    screen_color = pygame.Color("black")
    screen = makeScreen(screen_color, "PONG")
    game_logic = GameLogic(screen, screen_color)
    game_logic.game_logic()

    


if __name__ == "__main__":
    main()