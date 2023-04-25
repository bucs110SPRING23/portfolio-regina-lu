import pygame 

import pygame_menu

from snowman import Snowman

class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()

        ## Bouncing Ball Model
        self.ball = Ball(self.width / 2, self.height / 2, 100)
        self.sprites = pygame.sprite.Group((self.ball,))

    def mainloop(self):

        while self.state == "GAME":

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ball.rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

            self.sprites.update()

            # adjust the direction of the ball based on position
            if self.ball.rect.x < 0:
                self.ball.direction = "right"
            elif self.ball.rect.x > (self.width - self.ball.rect.width):
                self.ball.direction = "left"

            self.screen.fill("purple")

            self.sprites.draw(self.screen)

            pygame.display.flip()
    
    def __init__(self):
        pygame.init()
        ...
        self.state = "GAME"
    
    def gameloop(self):
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ball.rect.collidepoint(event.pos):
                        self.state = "END"
    def mainloop(self):
        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state =="END":
                self.endloop()
    def endloop(self):
        font_obj = pygame.font.SysFont(None, 48)
        msg = font_obj.render("You win! You may quit any time by closing the program", True, "yellow")

        while self.state == "END":

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            self.screen.blit(msg, (10, 10))
            pygame.display.flip()