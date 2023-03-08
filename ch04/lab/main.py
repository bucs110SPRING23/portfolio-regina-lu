import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode()
screen_size_variable = pygame.display.get_window_size()
screen = pygame.display.set_mode((screen_size_variable[1], screen_size_variable[1]))

screen.fill("gray")
pygame.display.flip()

pygame.draw.circle(screen, "pink", (screen_size_variable[1] / 2, screen_size_variable[1] / 2), screen_size_variable[1] / 2)
pygame.display.flip()

pygame.draw.line(screen, "black", (0, screen_size_variable[1] / 2), (screen_size_variable[1], screen_size_variable[1] / 2))
pygame.display.flip()

pygame.draw.line(screen, "black", (screen_size_variable[1] / 2, 0), (screen_size_variable[1] / 2, screen_size_variable[1]))
pygame.display.flip()
pygame.time.wait(2000)

pygame.draw.polygon(screen, "green", [(50, 50), (100, 50), (100, 100), (50, 100)])
pygame.display.flip()
pygame.time.wait(2000)

pygame.draw.polygon(screen, "blue", [(650, 50), (700, 50), (700, 100), (650, 100)])
pygame.display.flip()
pygame.time.wait(2000)

player1 = 0
player2 = 0

for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            (mousex, mousey) = pygame.mouse.get_pos()
            for tries in range(0,11):
                x = random.randint(0, screen_size_variable[1] + 1)
                y = random.randint(0, screen_size_variable[1] + 1)
                distance_from_center = math.hypot(x - screen_size_variable[1] / 2, y - screen_size_variable[1] / 2) #the distance formula
                is_in_circle = distance_from_center <= screen_size_variable[1]/2 #screen width
                if is_in_circle == True:
                    pygame.draw.circle(screen, "green", (x,y), 5)
                    player1 = player1 + 1
                    pygame.display.flip()
                    pygame.time.wait(1000)
                else:
                    pygame.draw.circle(screen, "red", (x,y), 5)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                x = random.randint(0, screen_size_variable[1] + 1)
                y = random.randint(0, screen_size_variable[1] + 1)
                distance_from_center = math.hypot(x - screen_size_variable[1] / 2, y - screen_size_variable[1] / 2) #the distance formula
                is_in_circle = distance_from_center <= screen_size_variable[1]/2 #screen width
                if is_in_circle == True:
                    pygame.draw.circle(screen, "blue", (x,y), 5)
                    player2 = player2 + 1
                    pygame.display.flip()
                    pygame.time.wait(1000)
                else:
                    pygame.draw.circle(screen, "white", (x,y), 5)
                    pygame.display.flip()
                    pygame.time.wait(1000)

if 50 <= mousex <= 100 and 50 <= mousey <= 100:
    if player1 > player2:
        font = pygame.font.Font(None, 48)
        text = font.render("PLAYER 1 WINS! You guessed correct!", True, "white")
        screen.blit(text, (50, screen_size_variable[1] / 2)) # where <x> and<y> are coordinates on screen
        pygame.display.flip()
        pygame.time.wait(1000)
    elif player1 < player2:
        font = pygame.font.Font(None, 48)
        text = font.render("PLAYER 2 WINS! You guessed incorrectly", True, "white")
        screen.blit(text, (50, screen_size_variable[1] / 2))
        pygame.display.flip()
        pygame.time.wait(1000)
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("TIE! You guessed incorrectly", True, "white")
        screen.blit(text, (50, screen_size_variable[1] / 2))
        pygame.display.flip()
        pygame.time.wait(1000)
elif 650 <= mousex <= 700 and 50 <= mousey <= 100:
    if player1 > player2:
        font = pygame.font.Font(None, 48)
        text = font.render("PLAYER 1 WINS! You guessed incorrectly!", True, "white")
        screen.blit(text, (50, screen_size_variable[1] / 2)) # where <x> and<y> are coordinates on screen
        pygame.display.flip()
        pygame.time.wait(1000)
    elif player1 < player2:
        font = pygame.font.Font(None, 48)
        text = font.render("PLAYER 2 WINS! You guessed correctly!", True, "white")
        screen.blit(text, (50, screen_size_variable[1] / 2))
        pygame.display.flip()
        pygame.time.wait(1000)
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("TIE! You guessed incorrectly!", True, "white")
        screen.blit(text, (50, screen_size_variable[1] / 2))
        pygame.display.flip()
        pygame.time.wait(1000)