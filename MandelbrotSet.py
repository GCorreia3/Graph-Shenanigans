# Import libraries
from PIL import Image

# Setup equations
equation = lambda z, c: z**2 + c

# Take in inputs
image_width = 1000
image_height = 1000
iterations = 100

image = Image.new("RGB", (image_width, image_height))

pixel_map = image.load()

# Setup Functions
def mandelbrot_set(f, iterations, c):
    # Initialises the first z value in the series (z0)
    z = 0

    # Repeatedly inputs zn into the function until the function either is too large(diverges) or it converges
    for i in range(iterations):
        if abs(z) >= 2:
            return False, i
        z = f(z, c)

    return abs(z) <= 2, iterations



for y in range(image_height):
    print(f"{100 * y / image_height}%")
    for x in range(image_width):
        c = complex(((x / image_width) * 4) - 2, ((y / image_height) * 4) - 2)
        converges, index = mandelbrot_set(equation, iterations, c)

        if converges:
            pixel_map[x, y] = (0, 0, 0)
        else:
            pixel_map[x, y] = (255, int(255 * (index / iterations)), int(255 * (index / iterations)))


#image.save("Mandelbrot3.png")
image.show()