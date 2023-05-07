import pygame
pygame.init()

# PART A
def threenp1(n):
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)    
        else:
            n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    threenp1range_iters_dict = {}
    for n in range(2, upper_limit + 1):
        iters = threenp1(n)
        threenp1range_iters_dict[n] = iters
    return threenp1range_iters_dict

# PART B
def graph_coordinates(threenplus1_iters_dict):
    coordinates = []
    for key,value in threenplus1_iters_dict.items():
        coordinates.append((key, value)) 

    display = pygame.display.set_mode()
    display.fill("red")
    pygame.draw.lines(display, "white", False, coordinates, width = 1)
    new_display = pygame.transform.flip(display, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width, height))
    display.blit(new_display, (0, 0))
    pygame.display.flip


    max_so_far = [0,0]
    for key, value in threenplus1_iters_dict.items():
        if value >= max_so_far[1]:
            max_so_far [1] = value
            max_so_far [0] = key

    font = pygame.font.Font(None, 50)
    msg = font.render("The largest number of iterations for the value " + str(max_so_far[0]) + " is " + str(max_so_far[1]), True, "white")
    display.blit(msg, (10,10))
    pygame.display.flip()
    pygame.time.wait(2000)

def main():
    #pygame.init()
    upperlimit = int(input("Enter an upper limit: "))
    print(threenp1range(upperlimit))
    graph_coordinates(threenp1range(upperlimit))

main()