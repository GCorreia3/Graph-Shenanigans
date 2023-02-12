import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors

f = lambda z, c: z**2 + c

x_start, y_start = -1.5, -1.5
width, height = 3, 3
resolution = 500
iterations = 200

# real and imaginary axis
real_axis = np.linspace(x_start, x_start + width, resolution)
imaginary_axis = np.linspace(y_start, y_start + height, resolution)

fig = plt.figure(figsize=(1, 1))
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

ax.clear()
ax.set_xticks([], [])
ax.set_yticks([], [])

# Create empty matrix
X = np.empty((len(real_axis), len(imaginary_axis)))

# iterations for the current threshold
for x in range(len(real_axis)):
    for y in range(len(imaginary_axis)):
        X[x, y] = mandelbrot(real_axis[x], imaginary_axis[y], iterations)


plt.imsave("MandelbrotZoomReference.png", arr=X.T, cmap=cmap)
