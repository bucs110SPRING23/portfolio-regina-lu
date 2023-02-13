import pygame
pygame.init()

screen = pygame.display.set_mode()

pygame.draw.circle(screen, 'red', [200, 150], 50)
pygame.display.flip()
pygame.time.wait(1000)

pygame.draw.circle(screen, 'red', [200, 250], 75)
pygame.display.flip()
pygame.time.wait(1000)

pygame.draw.circle(screen, 'red', [200, 375], 100)
pygame.display.flip()
pygame.time.wait(1000)