import random
import pygame

pygame.init()
screen = pygame.display.set_mode()
width, height = screen.get_window_size()

hitbox_width = width / 2
hitbox_height = height / 2

hitboxes = {
    "red": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "green": pygame.Rect(hitbox_width, 0, hitbox_width, hitbox_height),
    "blue": pygame.Rect(0, hitbox_height, hitbox_width, hitbox_height),
    "purple": pygame. Rect(hitbox_width, hitbox_height, hitbox_width, hitbox_height)
}

# Pygame Rect
# x and y coordinates
# width and height

# Rectangles do not track visuals

pygame.Rect(x, y, width, hitbox_height) 

hitboxes = {
    "red": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "green": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "blue": pygame.Rect(0, 0, hitbox_width, hitbox_height),
    "purple": pygame. Rect(0, 0, hitbox_width, hitbox_height)
}

hitboxes["blue"], topleft = hitboxes["red"].topright
hitboxes["green"], topright = hitboxes["red"].bottomright
hitboxes["purple"], topright = hitboxes["red"].bottomright

font = pygame.font.SysFont("Arial", 24)

done = False
result = []
turns = 0
order = list(hitboxes.keys())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            turns = turns - 1
            if hitboxes["red"].collidepoint(event.pos):
                result.append("red")
            elif hitboxes["green"].collidepoint(event.pos):
                result.append("green")
            elif hitboxes["green"].collidepoint(event.pos):
                result.append("green")