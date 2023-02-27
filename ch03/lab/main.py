# Part A
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode()
screen_size_variable = pygame.display.get_window_size()

screen.fill("blue")
pygame.display.flip()
pygame.time.wait(2000)

pygame.draw.circle(screen, "Pink", (screen_size_variable[0] / 2, screen_size_variable[1] / 2), screen_size_variable[1] / 2)
pygame.display.flip()
pygame.time.wait(2000)

pygame.draw.line(screen, "black", )
pygame.display.flip()
pygame.time.wait(2000)

# Part B
distance_from_center = math.hypot(x1-x2, y1-y2) #the distance formula
is_in_circle = distance_from_center <= width/2 #screen width