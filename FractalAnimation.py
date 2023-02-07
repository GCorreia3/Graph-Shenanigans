import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

f = lambda z, c: z**3 + c

x_start, y_start = -1, -1.5
width, height = 2, 3
density_per_unit = 300

# real and imaginary axis
real_axis = np.linspace(x_start, x_start + width, width * density_per_unit)
imaginary_axis = np.linspace(y_start, y_start + height, height * density_per_unit)

fig = plt.figure(figsize=(10, 10))
ax = plt.axes()

def mandelbrot(x, y, threshold):
    # initial conditions
    c = complex(x, y)
    z = complex(0, 0)
    
    for i in range(threshold):
        if abs(z) > 4:
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
    

    img = ax.imshow(X.T, interpolation="bicubic", cmap='magma')
    return [img]
 
anim = animation.FuncAnimation(fig, animate, frames=45, interval=120, blit=True)
anim.save('mandelbrot3.gif')