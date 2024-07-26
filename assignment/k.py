import numpy as np


def f(x, y):
    return x**2 + y**2 - x * y + x - y + 1


def gradient_f(x, y):
    dx = 2 * x - y + 1
    dy = 2 * y - x - 1
    return np.array([dx, dy])


def gradient_descent(learning_rate=0.1, num_iterations=1000, tolerance=1e-6):
    x, y = 0, 0  # Starting point (0, 0)

    for _ in range(num_iterations):
        grad = gradient_f(x, y)
        new_x = x - learning_rate * grad[0]
        new_y = y - learning_rate * grad[1]

        if np.abs(f(new_x, new_y) - f(x, y)) < tolerance:
            break

        x, y = new_x, new_y

    return x, y, f(x, y)


# Run gradient descent
x_min, y_min, f_min = gradient_descent()
print(f"Minimum found at x = {x_min}, y = {y_min}")
print(f"Minimum value of f(x, y) = {f_min}")
