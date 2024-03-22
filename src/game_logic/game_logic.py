from enum import Enum
import pygame
from src.paddle.paddle import Paddle
from src.fps.fps import FPS
from src.ball.ball import Ball


PADDLE_SPACING = 20

class GameState(Enum):
    START_MENU = 0
    GAME_PLAYING = 1
    GAME_OVER = 2

class GameLogic:
    screen: pygame.Surface
    screen_color: pygame.Color
    screen_height: int
    screen_width: int
    score_p1: int
    score_p2: int


    def __init__(self, screen: pygame.Surface, screen_color: pygame.Color) -> None:
        self.score_p1 = 0
        self.score_p2 = 0
        self.screen = screen
        self.game_state = GameState.START_MENU
        self.screen_color = screen_color
        self.screen_width, self.screen_height = self.screen.get_size()
    
    def __str__(self) -> str:
        res = self.__class__.__name__ + '(' + \
            ', '.join('%s=%s' % item for item in vars(self).items()) + ')'
        return res

    def __scored(self, ball: Ball) -> bool:
        ret = False
        width, _ = self.screen.get_size()
        if ball.circle.left == 0:
            self.score_p2 += 1
            ret = True
        if ball.circle.right == width:
            self.score_p1 += 1
            ret = True
        return ret
    
    def __draw_score(self):
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("P1: {} - P2: {}".format(self.score_p1, self.score_p2), True, pygame.Color("white"))
        textRect = text.get_rect()
        textRect.center = (self.screen_width // 2, PADDLE_SPACING)
        self.screen.blit(text, textRect)
    
    def __draw_start_menu(self):
        font = pygame.font.Font("freesansbold.ttf", 100)
        title = font.render("PONG", True, pygame.Color("white"))
        titleRect = title.get_rect()
        titleRect.center = self.screen_width // 2, 100
           
        font_button = pygame.font.Font("freesansbold.ttf", 40)
        start_button = font_button.render("Press Space To Start", True, pygame.Color("white"))
        start_button_rect = start_button.get_rect()
        start_button_rect.center = self.screen_width // 2, titleRect.bottom + 50
        self.screen.blit(title, titleRect)
        return self.screen.blit(start_button, start_button_rect)

    def __draw_end_screen(self):
        winner = "Player 1" if self.score_p1 == 3 else "Player 2"
        font = pygame.font.Font("freesansbold.ttf", 100)
        title = font.render("{} WINS!!".format(winner), True, pygame.Color("white"))
        title_rect = title.get_rect()
        title_rect.center = self.screen_width // 2, 100

        font = pygame.font.Font("freesansbold.ttf", 40)
        quit_opt = font.render("ESQ - Quit", True, pygame.Color("white"))
        restart_opt = font.render("SpaceBar - to play again", True, pygame.Color("white"))
        quit_opt_rect, restart_opt_rec = quit_opt.get_rect(), restart_opt.get_rect()
        quit_opt_rect.center = self.screen_width // 2, title_rect.bottom + 50
        restart_opt_rec.center = self.screen_width // 2, quit_opt_rect.bottom + 50

        self.screen.blit(title, title_rect)
        self.screen.blit(quit_opt, quit_opt_rect)
        self.screen.blit(restart_opt, restart_opt_rec)

    
    def main_loop(self):
        fps = FPS()
        paddle_left = Paddle(
            self.screen, 
            pygame.K_w, 
            pygame.K_s, 
            pygame.Color("white"), 
            [PADDLE_SPACING, self.screen_height//2])
        paddle_right = Paddle(
            self.screen, 
            pygame.K_UP, 
            pygame.K_DOWN, 
            pygame.Color("white"),
            [self.screen_width - (PADDLE_SPACING + 20), self.screen_height//3])
        
        ball = Ball(
            self.screen, 
            [self.screen_height//2, self.screen_height//2], 
            pygame.Color("white"), 
            15)

        # Variable to keep our game loop running 
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_ESCAPE]:
                    running = False

            self.screen.fill(self.screen_color) # Clear the screen


            match self.game_state:
                case GameState.START_MENU:
                    self.__draw_start_menu()
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        self.game_state = GameState.GAME_PLAYING
                    
                case GameState.GAME_PLAYING:
                    fps.clock.tick(180)
                    fps.render(self.screen)
                    paddle_left.update()
                    paddle_right.update()
                    ball.update(paddle_left, paddle_right)
                    should_reset = self.__scored(ball)
                    if should_reset:
                        ball.circle.center = (self.screen_height//2, self.screen_height//2)
                    if self.score_p1 == 3 or self.score_p2 == 3:
                        self.game_state = GameState.GAME_OVER
                    ball.draw_ball()
                    self.__draw_score()
                case _:
                    self.__draw_score()
                    self.__draw_end_screen()
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        paddle_left.reset_pos([PADDLE_SPACING, self.screen_height//2])
                        paddle_right.reset_pos([self.screen_width - (PADDLE_SPACING + 20), self.screen_height//3])
                        ball.circle.center = (self.screen_height//2, self.screen_height//2)
                        self.score_p1 = 0
                        self.score_p2 = 0
                        self.game_state = GameState.GAME_PLAYING

                

            paddle_left.draw_paddle()
            paddle_right.draw_paddle()
                

            pygame.display.update()

        print("Quitting game")

    