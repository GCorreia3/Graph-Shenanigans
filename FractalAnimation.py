import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors

f = lambda z, c: z**2 + c

x_start, y_start = -2, -1.5
width, height = 3, 3
density_per_unit = 250

# real and imaginary axis
real_axis = np.linspace(x_start, x_start + width, width * density_per_unit)
imaginary_axis = np.linspace(y_start, y_start + height, height * density_per_unit)

fig = plt.figure(figsize=(10, 10))
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()

fig.add_axes(ax)

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["blue", "green", "yellow", "red", "white", "black"])

def mandelbrot(x, y, threshold):
    # initial conditions
    c = complex(x, y)
    z = complex(0, 0)
    
    for i in range(threshold):
        if abs(z) > 2:
            return i
        z = f(z, c)
        
    return threshold - 1

def animate(i):
    ax.clear()
    ax.set_xticks([], [])
    ax.set_yticks([], [])
    
    # Create empty matrix
    X = np.empty((len(real_axis), len(imaginary_axis)))
    threshold = round(1.15**(i + 1))
    
    # iterations for the current threshold
    for x in range(len(real_axis)):
        for y in range(len(imaginary_axis)):
            X[x, y] = mandelbrot(real_axis[x], imaginary_axis[y], threshold)
    

    img = ax.imshow(X.T, interpolation="bicubic", cmap=cmap)
    return [img]
 
anim = animation.FuncAnimation(fig, animate, frames=20, interval=120, blit=True)
anim.save('mandelbrot4.gif')