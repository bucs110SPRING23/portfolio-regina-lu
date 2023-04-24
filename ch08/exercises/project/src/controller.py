import pygame 

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display
        self.background_color = (200, 200, 250)
        self.background.fill(self.background_color)
        self.snowpeoples
        self.max_snowpeoples = 20
        number_of_snowpeoples = 2
        interval = self.screen.get_width() // (number_of_snowpeoples + 1)
        x = interval
        for _ in range(number_of_snowpeoples):
            

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type ==
