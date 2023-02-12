# Import libraries
import pygame
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

pygame.init()

running = True

# Setup equations
equation = lambda z, c: z**2 + c

x_start, y_start = -1.5, -1.5
zoom = 1
dz = 1
start_width = 3
width = lambda zoom: start_width / zoom
resolution = 500
iterations = 100

# real and imaginary axis
real_axis = lambda x, w, r: np.linspace(x, x + w, r)
imaginary_axis = lambda y, w, r: np.linspace(y, y + w, r)

fig = plt.figure(figsize=(1, 1))
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()

fig.add_axes(ax)

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["blue", "green", "yellow", "red", "white", "black"])

# Take in inputs
screen_width = resolution
screen_height = resolution
win = pygame.display.set_mode((screen_width, screen_height))

rect_width = 100
rect_height = 100

mandelbrot_image = pygame.image.load('MandelbrotZoomReference.png')

last_zoom_pos = complex(0, 0)

# Setup Functions
def mandelbrot(f, x, y, threshold):
    # initial conditions
    c = complex(x, y)
    z = complex(0, 0)
    
    for i in range(threshold):
        if abs(z) > 2:
            return i
        z = f(z, c)
        
    return threshold - 1

def draw_mandelbrot():
    mouse = pygame.mouse.get_pos()

    zoom_pos = screen_pos_to_complex(mouse)

    global last_zoom_pos
    last_zoom_pos = zoom_pos
    
    global dz
    global zoom
    zoom += dz
    dz *= 2

    ax.clear()
    ax.set_xticks([], [])
    ax.set_yticks([], [])

    print(zoom_pos.real - (width(zoom) / 2), width(zoom), zoom_pos.imag - (width(zoom) / 2))

    r_axis = real_axis(zoom_pos.real - (width(zoom) / 2), width(zoom), resolution)
    i_axis = imaginary_axis(zoom_pos.imag - (width(zoom) / 2), width(zoom), resolution)

    # Create empty matrix
    X = np.empty((len(r_axis), len(i_axis)))

    # iterations for the current threshold
    for x in range(len(r_axis)):
        for y in range(len(i_axis)):
            X[x, y] = mandelbrot(equation, r_axis[x], i_axis[y], iterations)


    plt.imsave("MandelbrotZoom.png", arr=X.T, cmap=cmap)



def screen_pos_to_complex(pos):
    return complex(((pos[0] / screen_width) * width(zoom) - (width(zoom) / 2) + last_zoom_pos.real),
                   ((pos[1] / screen_height) * width(zoom) - (width(zoom) / 2) + last_zoom_pos.imag))

def draw_screen():
    win.blit(mandelbrot_image, (0, 0))

    pygame.display.update()

def quit():
    pygame.quit()
    sys.exit(0)

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
            draw_mandelbrot()
            mandelbrot_image = pygame.image.load("MandelbrotZoom.png")

