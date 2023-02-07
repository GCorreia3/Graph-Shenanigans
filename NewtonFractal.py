# Import libraries
from PIL import Image
import math, datetime

# Setup equations
# equation = lambda x: 3*x**3 + 6*x**2 - x - 20
# derived_equation = lambda x: 9*x**2 + 12*x - 1
equation = lambda x: x**5 - 5*x**4 + 39*x**3 + 105*x**2 - 700*x + 5000
derived_equation = lambda x: 5*x**4 - 20*x**3 + 117*x**2 + 210*x - 700
# equation = lambda x: x**4 + 4
# derived_equation = lambda x: 4*x**3

# roots = [complex(1.4412, 0), complex(-1.7206, 1.2906), complex(-1.7206, -1.2906)]
roots = [complex(2, -6), complex(2, 6), complex(-5, 0), complex(3, 4), complex(3, -4)]
# roots = [complex(1, 1), complex(1, -1), complex(-1, 1), complex(-1, -1)]# 

colours = [(162, 250, 163), (146, 201, 177), (79, 117, 155), (93, 81, 121), (87, 31, 78)]
# colours = [(22, 105, 122), (255, 166, 43), (237, 231, 227), (130, 192, 204)]

# Take in inputs
image_width = 4000
image_height = 4000
guess_iteration = 50

image = Image.new("RGB", (image_width, image_height))

pixel_map = image.load()

# Setup Functions
def fast_newton_raphson(f, f_prime, iterations, guess):
    # Initialises start x value (x nought)
    x = guess

    # Loops through to make x get increasingly closer to a root
    for i in range(iterations):
        gradient = f_prime(x)

        # Prevents divide by 0 error
        if gradient != 0:
            step = f(x) / gradient
            if step == 0:
                return (x, i)
            x = x - step
        else:
            return (x, i)

    # Print final x value after iterating
    return (x, iterations)

def distance_between_complex_number(z1, z2):
    return abs(z1 - z2)
    # return (z2.real - z1.real)**2 + (z2.imag - z1.imag)**2


# Main loop:
# Loops through all of the pixels of the image you want to make, and asigns a complex number to them
# Then find the root that the complex number is closest to after a certain number of iterations
# Finally, set the colour of that pixel to the colour of the root that it was closest to

print(datetime.datetime.now())

for y in range(image_height):
    print(f"{100 * y / image_height}%")
    for x in range(image_width):
        # z = complex(x - (image_width / 2), y - (image_height / 2))
        z = complex(((x / image_width) * 64) - 32, ((y / image_height) * 64) - 32)
        root, num_iters = fast_newton_raphson(equation, derived_equation, guess_iteration, z)
        if num_iters == 0:
            num_iters = 1

        final_root = None

        dist = math.inf

        for i, r in enumerate(roots):
            col = colours[i]
            # new_col = tuple(component * (num_iters/guess_iteration) for component in col)
            new_col = tuple(component * (guess_iteration / (num_iters * 10)) for component in col)
            new_col = tuple(int(x) for x in new_col)

            complex_dist = distance_between_complex_number(root, r)
            if complex_dist == 0:
                final_root = r
                pixel_map[x, y] = new_col
                break
            
            elif complex_dist < dist:
                dist = complex_dist
                final_root = r
                pixel_map[x, y] = new_col

print(datetime.datetime.now())

#image.save("Fractal10.png")
image.show()