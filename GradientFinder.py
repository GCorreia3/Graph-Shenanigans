# Import libraries
import matplotlib.pyplot as plt
import math, random

# Setup equations
equation = lambda x: 3*x**3 + 6*x**2 - x - 20
derived_equation = lambda x: 9*x**2 + 12*x - 1

precision = "%.2f"

# Take in inputs
start_x = float(input("Enter start value: "))
end_x = float(input("Enter end value: "))
step = float(input("Enter step value: "))
x_gradient = float(input("X point of gradient: "))

print("\n")

# Setup Functions
def compute_gradient(f, x_pos):
    x_difference = (x_pos + 0.000001) - x_pos
    y_difference = f(x_pos + 0.000001) - f(x_pos)

    return y_difference / x_difference

def get_gradient(x_pos):
    return derived_equation(x_pos)

def find_y_intercept(gradient, x_position):
    y_height = equation(x_position)

    return y_height - gradient * x_position

def create_line(f, start_x, end_x, x_array, y_array, dx):
    x = start_x

    # Loops through all of the x values and calculates the corresponding y value until you reach the end x value

    while x <= end_x:
        y = f(x)
        y_array.append(y)
        x_array.append(x)
        x = float("%.2f" % (x + dx))


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


# Make gradient line

gradient = get_gradient(x_gradient)

rounded_gradient = float(precision % gradient)

print(f"Gradient: {rounded_gradient}")

y_intercept = find_y_intercept(rounded_gradient, x_gradient)

gradient_equation = lambda x: rounded_gradient*x + y_intercept

y_gradient = []
x_gradient = []

if rounded_gradient > 0:
    ex = (y_min - y_intercept) / rounded_gradient
    x_finish = (y_max - y_intercept) / rounded_gradient
elif rounded_gradient == 0:
    ex = start_x
    x_finish = end_x
elif rounded_gradient < 0:
    ex = (y_max - y_intercept) / rounded_gradient
    x_finish = (y_min - y_intercept) / rounded_gradient

create_line(gradient_equation, ex, x_finish, x_gradient, y_gradient, 0.5)



def plot():
    # Curve plot
    #plt.plot(x_array, y_array, color='blue', marker='.', markerfacecolor='red', markeredgecolor='red')
    plt.plot(x_array, y_array, color='blue')

    # Axis plot
    plt.plot(x_horizontal, y_horizontal, color='black')
    plt.plot(x_vertical, x_vertical, color='black')

    # Gradient line plot
    plt.plot(x_gradient, y_gradient, color='green', label=f'Gradient: {rounded_gradient}')

    plt.title("Equation Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

# Finally, plot all of the values
plot()