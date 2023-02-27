# Part A
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode()
screen_size_variable = pygame.display.get_window_size()
screen = pygame.display.set_mode((screen_size_variable[1], screen_size_variable[1]))

screen.fill("blue")
pygame.display.flip()

pygame.draw.circle(screen, "pink", (screen_size_variable[1] / 2, screen_size_variable[1] / 2), screen_size_variable[1] / 2)
pygame.display.flip()

pygame.draw.line(screen, "black", (0, screen_size_variable[1] / 2), (screen_size_variable[1], screen_size_variable[1] / 2))
pygame.display.flip()

pygame.draw.line(screen, "black", (screen_size_variable[1] / 2, 0), (screen_size_variable[1] / 2, screen_size_variable[1]))
pygame.display.flip()
pygame.time.wait(2000)

# Part B
for tries in range(0,11):
    x = random.randint(0, screen_size_variable[1] + 1)
    y = random.randint(0, screen_size_variable[1] + 1)
    distance_from_center = math.hypot(x - screen_size_variable[1] / 2, y - screen_size_variable[1] / 2) #the distance formula
    is_in_circle = distance_from_center <= screen_size_variable[1]/2 #screen width
    if is_in_circle == True:
        pygame.draw.circle(screen, "green", (x,y), 5)
        pygame.display.flip()
        pygame.time.wait(1000)
    else:
        pygame.draw.circle(screen, "red", (x,y), 5)
        pygame.display.flip()
        pygame.time.wait(1000)
