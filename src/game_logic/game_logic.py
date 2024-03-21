import pygame
from src.paddle.paddle import Paddle
from src.fps.fps import FPS
from src.ball.ball import Ball


PADDLE_SPACING = 20

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
            self.score_p1 += 1
            ret = True
        if ball.circle.right == width:
            self.score_p2 += 1
            ret = True
        return ret
    
    def __draw_score(self):
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("P1: {} - P2: {}".format(self.score_p1, self.score_p2), True, pygame.Color("white"))
        textRect = text.get_rect()
        textRect.center = (self.screen_width // 2, PADDLE_SPACING)
        self.screen.blit(text, textRect)
    
    def game_logic(self):
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
            pygame.Color("white"),[
            self.screen_width - (PADDLE_SPACING + 20), int(self.screen_height/1.5)])
        
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
            fps.clock.tick(180)
            fps.render(self.screen)
            paddle_left.update()
            paddle_right.update()
            ball.update(paddle_left, paddle_right)
            should_reset = self.__scored(ball)
            if should_reset:
                ball.circle.center = (self.screen_height//2, self.screen_height//2)
            if self.score_p1 == 2 or self.score_p2 == 2:
                running = False
            paddle_left.draw_paddle()
            paddle_right.draw_paddle()
            ball.draw_ball()
            self.__draw_score()

            pygame.display.update()

        print("Quitting game")

    