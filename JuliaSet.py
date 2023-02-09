# Import libraries
from PIL import Image

# Setup equations
equation = lambda z: z**2 + complex(0.35, 0.35)

# Take in inputs
image_width = 1000
image_height = 1000
iterations = 100

image = Image.new("RGB", (image_width, image_height))

pixel_map = image.load()

# Setup Functions
def julia_set(f, iterations, z0):
    # Initialises the first z value in the series (z0)
    z = z0

    # Repeatedly inputs zn into the function until the function either is too large(diverges) or it converges
    for i in range(iterations):
        if abs(z) > 2:
            return False, i
        z = f(z)

    return abs(z) <= 2, iterations



for y in range(image_height):
    print(f"{100 * y / image_height}%")
    for x in range(image_width):
        z0 = complex(((x / image_width) * 4) -2, ((y / image_height) * 4) - 2)

        converges, index = julia_set(equation, iterations, z0)

        if converges:
            pixel_map[x, y] = (0, 0, 0)
        else:
            pixel_map[x, y] = (255, int(255 * (index / iterations)), int(255 * (index / iterations)))


#image.save("Juliaset2.png")
image.show()