# Import libraries
import pygame
import sys
import math

pygame.init()

running = True

# Setup equations
equation = lambda z, c: z**2 + c

# Take in inputs
screen_width = 1000
screen_height = 1000
win = pygame.display.set_mode((screen_width, screen_height))

zoom = 4

x_width = zoom
y_width = zoom

background_colour = (0, 0, 0)

iterations = 10

solutions = []

c_position = complex(0.5, 0.5)
z0_position = complex(-0.5, -0.5)

moving_c = False
moving_z0 = False

# Setup Functions
def mandelbrot_set(f, iterations, z0, c):
    # Initialises the first z value in the series (z0)
    z = z0

    for i in range(iterations):
        z = f(z, c)

    return z

def create_solutions():
    solutions.clear()
    solutions.append(z0_position)
    for i in range(iterations):
        solutions.append(mandelbrot_set(equation, i, z0_position, c_position))

def get_screen_pos(num):
    return ((num.real * (screen_width / x_width)) + 0.5*screen_width, (num.imag * (screen_height / y_width)) + 0.5*screen_height)

def screen_pos_to_complex(pos):
    return complex(((pos[0] / screen_width) * zoom) - (zoom / 2), ((pos[1] / screen_height) * zoom) - (zoom / 2))

def dist_between_tuple(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def mouse_click(mouse):
    global moving_c
    global moving_z0
    if dist_between_tuple(get_screen_pos(c_position), mouse) < 15:
        moving_c = True
    elif dist_between_tuple(get_screen_pos(z0_position), mouse) < 15:
        moving_z0 = True

def mouse_moved(mouse):
    global c_position
    global z0_position
    if moving_c:
        c_position = screen_pos_to_complex(mouse)
        create_solutions()
    elif moving_z0:
        z0_position = screen_pos_to_complex(mouse)
        create_solutions()

def draw_screen():

    win.fill(background_colour)

    # Y axis
    pygame.draw.line(win, (255, 255, 255), (screen_width / 2, 0), (screen_width / 2, screen_height), 1)

    # X axis
    pygame.draw.line(win, (255, 255, 255), (0, screen_height / 2), (screen_width, screen_height / 2), 1)

    for i in range(len(solutions) - 1):
        pygame.draw.line(win, (255, 255, 255), get_screen_pos(solutions[i]), get_screen_pos(solutions[i+1]), 2)

    for solution in solutions:
        pygame.draw.circle(win, (255, 0, 0), get_screen_pos(solution), 60 / zoom)

    # Draw c
    pygame.draw.circle(win, (0, 255, 0), get_screen_pos(c_position), 60 / zoom)

    # Draw z0
    pygame.draw.circle(win, (0, 0, 255), get_screen_pos(z0_position), 60 / zoom)

    pygame.display.update()

def quit():
    pygame.quit()
    sys.exit(0)

create_solutions()

# Main loop
while running:

    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()

        elif event.type == pygame.QUIT:
            quit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse = pygame.mouse.get_pos()
            mouse_click(mouse)

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            moving_c = False
            moving_z0 = False

        elif event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            mouse_moved(mouse)

