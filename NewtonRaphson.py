# Import libraries
import matplotlib.pyplot as plt
import math, random

# Setup equations
equation = lambda x: 3*x**3 + 6*x**2 - x - 20
derived_equation = lambda x: 9*x**2 + 12*x - 1
# equation = lambda x: x**5 - 5*x**4 + 39*x**3 + 105*x**2 - 700*x + 5000
# derived_equation = lambda x: 5*x**4 - 20*x**3 + 117*x**2 + 210*x - 700

precision = "%.2f"

# Take in inputs
start_x = float(input("Enter start value: "))
end_x = float(input("Enter end value: "))
step = float(input("Enter step value: "))
root_guess = float(input("Initial Root Guess: "))
guess_iteration = int(input("Guess iteration: "))

print("\n")

# Setup Functions

def get_gradient(x_pos):
    return derived_equation(x_pos)

def create_line(f, start_x, end_x, x_array, y_array, dx):
    x = start_x

    # Loops through all of the x values and calculates the corresponding y value until you reach the end x value

    while x <= end_x:
        y = f(x)
        y_array.append(y)
        x_array.append(x)
        x = float("%.2f" % (x + dx))

def newton_raphson(f, iterations):

    # Loop through by a set number of times stated with the variable guess_iteration
    for i in range(iterations):
        """
            Note: we are uing the (2 * i)th value in our array since each iterration we will append 2 new
            x positions, each of which are the exact same. They are still required in drawing the lines. 
        """

        # Calculate the y position of the x intercept of the previous iteration
        # The x intercept will be the start_x value if it is the first iteration
        start_y_val = f(raphson_x[2*i])

        # Append the x and y position of the point on the curve
        raphson_x.append(raphson_x[2*i])
        raphson_y.append(start_y_val)

        # Get the gradient of this point on the curve
        gradient = get_gradient(raphson_x[2*i])

        # Calculate the y intercept of the new gradient at the x, y position on the curve
        y_intercept = raphson_y[2*i+1] - (gradient * raphson_x[2*i+1])

        # Calculate the x intercept by setting y = 0 in the equation of the gradient line
        # Then rearange to find x
        x_intercept = -y_intercept / gradient

        # Append the new x and y position of the x curve gradient crossing the x axis
        raphson_x.append(x_intercept)
        raphson_y.append(0)

def fast_newton_raphson(f, f_prime, iterations, guess):
    # Initialises start x value (x nought)
    x = guess

    # Loops through to make x get increasingly closer to a root
    for i in range(iterations):
        x = x - (f(x) / f_prime(x))

    # Print final x value after iterating
    print(x)



x_array = []
y_array = []

dx = float(precision % step)

create_line(equation, start_x, end_x, x_array, y_array, dx)


# Create Axis
x_horizontal = [start_x, end_x]
y_horizontal = [0, 0]

y_min = min(y_array)
if y_min > 0:
    y_min = 0

y_max = max(y_array)
if y_max < 0:
    y_max = 0

x_vertical = [0, 0]
y_vertical = [y_min, y_max]


# Set up start coordinates for newton raphson

raphson_x = []
raphson_y = []

# Add first coordinate to the raphson arrays
raphson_x.append(root_guess)
raphson_y.append(0)

# Find roots
newton_raphson(equation, guess_iteration)

# Fast Newton Raphson
fast_newton_raphson(equation, derived_equation, guess_iteration, root_guess)

print(f"Root Guess: {raphson_x[len(raphson_x) - 1]}")

def plot():
    # Curve plot
    #plt.plot(x_array, y_array, color='blue', marker='.', markerfacecolor='red', markeredgecolor='red')
    plt.plot(x_array, y_array, color='blue')

    # Axis plot
    plt.plot(x_horizontal, y_horizontal, color='black')
    plt.plot(x_vertical, x_vertical, color='black')

    # Newton raphson plot
    plt.plot(raphson_x, raphson_y, color='red', label='Newton Raphson Root Finding')

    plt.title("Equation Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

# Finally, plot all of the values
plot()