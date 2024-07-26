import numpy as np
import matplotlib.pyplot as plt

# Given data points
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])


# 1. Lagrange Polynomial Interpolation
def lagrange_interpolation(x, y):
    def L(x, i):
        L = np.ones_like(x)
        for j in range(len(x_data)):
            if i != j:
                L *= (x - x_data[j]) / (x_data[i] - x_data[j])
        return L

    def P(x):
        return sum(y_data[i] * L(x, i) for i in range(len(x_data)))

    return P


# 2. Newton's Divided Difference Method
def newton_divided_difference(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    def P(x_val):
        n = len(x_data) - 1
        p = coef[0][0]
        for i in range(1, n + 1):
            term = coef[0][i]
            for j in range(i):
                term *= x_val - x_data[j]
            p += term
        return p

    return P, coef[0]


# 3. Compare the methods
x_data, y_data = x, y

# Lagrange method
P_lagrange = lagrange_interpolation(x_data, y_data)

# Newton's method
P_newton, coef_newton = newton_divided_difference(x_data, y_data)

# Generate points for plotting
x_plot = np.linspace(0, 5, 100)
y_lagrange = [P_lagrange(xi) for xi in x_plot]
y_newton = [P_newton(xi) for xi in x_plot]

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, color="red", label="Data points")
plt.plot(x_plot, y_lagrange, label="Lagrange Polynomial")
plt.plot(x_plot, y_newton, "--", label="Newton's Polynomial")
plt.legend()
plt.title("Comparison of Lagrange and Newton Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("/assets/i-Newton-Interpolation.png")

print("Newton's Divided Difference Coefficients:", coef_newton)

# Evaluate at a new point
x_new = 2.5
print(f"\nValue at x = {x_new}:")
print(f"Lagrange: {P_lagrange(x_new)}")
print(f"Newton: {P_newton(x_new)}")
