import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])


def linear_interpolation(x0, x1, y0, y1, x):
    """Linear interpolation between two points."""
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)


# Find the two points between which x=4.0 lies
i = np.searchsorted(x, 4.0) - 1
x0, x1 = x[i], x[i + 1]
y0, y1 = y[i], y[i + 1]

# Interpolate to find y at x=4.0
y_interpolated = linear_interpolation(x0, x1, y0, y1, 4.0)

print(f"The interpolated y-value at x=4.0 is: {y_interpolated:.4f}")

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(x, y, "bo-", label="Given points")
plt.plot([4.0], [y_interpolated], "ro", label="Interpolated point")
plt.plot([x0, x1], [y0, y1], "g-", label="Interpolation segment")
plt.xlabel("X (in)")
plt.ylabel("Y (in)")
plt.title("Linear Interpolation for Robot Laser Scanner")
plt.legend()
plt.grid(True)
plt.savefig("./assets/c-linear_interpolation.png")
