import pygame

pygame.init()
screen = pygame.display.set_mode()
screen.fill("red")
pygame.display.flip()
input("Press Enter to continue...")
screen.fill("green")
pygame.display.flip()
input("Press Enter to continue...")

# keeps track of display image and next image