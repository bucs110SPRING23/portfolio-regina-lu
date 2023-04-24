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
    for n in range(2,upper_limit + 1):
        iters = threenp1(n)
        threenp1range_iters_dict[n] = iters
    return threenp1range_iters_dict

# PART B
def graph_coordinates(threenplus1_iters_dict):
    coordinates = threenplus1_iters_dict.items()
    for i in coordinates:
        print(i)  

display = pygame.display.set_mode()
new_display = pygame.transform.flip(display, False, True)
width, height = new_display.get_size()
new_display = pygame.transform.scale(new_display, (width * 5, height * 5))

display.blit(new_display, (0, 0))

def maxnum(threenplus1_iters_dict):
    max_so_far = 0
    for item in threenplus1_iters_dict.values():
        if item > max_so_far:
            max_so_far = max_so_far
    return max_so_far

max_so_far = str(maxnum(threenp1range(10)))

font = pygame.font.Font(None, 50)
msg = font.render(max_so_far, True, "white")
display.blit(msg, (10,10))

def main():
    print(threenp1(21))
    print(threenp1range(25))
    graph_coordinates(threenp1range(10))
    maxnum(threenp1range(10))

main()