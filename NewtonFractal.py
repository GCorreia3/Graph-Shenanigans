# Import libraries
from PIL import Image
import math

# Setup equations
equation = lambda x: 3*x**3 + 6*x**2 - x - 20
derived_equation = lambda x: 9*x**2 + 12*x - 1

roots = [complex(1.4412, 0), complex(-1.7206, 1.2906), complex(-1.7206, -1.2906)]

colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

precision = "%.2f"

# Take in inputs
image_width = 4000
image_height = 4000
guess_iteration = 300

image = Image.new("RGB", (image_width, image_height))

pixel_map = image.load()

# Setup Functions
def fast_newton_raphson(f, f_prime, iterations, guess):
    # Initialises start x value (x nought)
    x = guess

    # Loops through to make x get increasingly closer to a root
    for i in range(iterations):
        x = x - (f(x) / f_prime(x))

    # Print final x value after iterating
    return x

def distance_between_complex_number(z1, z2):
    return math.sqrt((z2.real - z1.real)**2 + (z2.imag + z1.imag)**2)


# Main loop:
# Loops through all of the pixels of the image you want to make, and asigns a complex number to them
# Then find the root that the complex number is closest to after a certain number of iterations
# Finally, set the colour of that pixel to the colour of the root that it was closest to

for y in range(image_height):
    for x in range(image_width):
        z = complex(x - (image_width / 2), y - (image_height / 2))
        root = fast_newton_raphson(equation, derived_equation, guess_iteration, z)

        final_root = None

        dist = math.inf

        for i, r in enumerate(roots):
            complex_dist = distance_between_complex_number(root, r)
            if complex_dist < dist:
                dist = complex_dist
                final_root = r
                pixel_map[x, y] = colours[i]

image.save("Fractal2.png")
image.show()