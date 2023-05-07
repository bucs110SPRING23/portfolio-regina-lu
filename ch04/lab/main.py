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

player1_box = pygame.draw.rect(screen, "green", (50,50,100,100))
player2_box = pygame.draw.rect(screen, "blue", (250,50,100,100))

font = pygame.font.Font(None, 30)
text = font.render("Select the winning player:", True, "white")
screen.blit(text, (50, 25))
pygame.display.flip()

player1 = 0
player2 = 0

selected_player = None
game_result = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if (player1_box.collidepoint(mouse_position)) or (player2_box.collidepoint(mouse_position)):
                if (player1_box.collidepoint(mouse_position)):
                    selected_player = "player1"
                elif (player2_box.collidepoint(mouse_position)):
                    selected_player = "player2"
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
    if selected_player:
        if player1 > player2:
            game_result = "player1"
            if selected_player == game_result:
                guess_result = "Green won. You have guessed correctly!"
            else:
                guess_result = "Blue won. You have guessed incorrectly."
        elif player1 < player2:
            game_result = "player2"
            if selected_player == game_result:
                guess_result = "Blue won. You have guessed correctly!"
            else:
                guess_result = "Green won. You have guessed incorrectly."
        else:
            game_result = "Incorrect, it was a tie!"
        font = pygame.font.Font(None, 30)
        result_text = font.render(f"Game result: {guess_result}", True, "black")
        screen.blit(result_text, (50, screen_size_variable[1] / 2))
        pygame.display.flip()
        pygame.time.wait(1000)