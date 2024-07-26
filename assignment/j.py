import numpy as np


def power_iteration(A, num_iterations=1000, tolerance=1e-8):
    n = A.shape[0]
    v = np.random.rand(n)
    v = v / np.linalg.norm(v)

    for _ in range(num_iterations):
        Av = A @ v
        eigenvalue = v.T @ Av
        new_v = Av / np.linalg.norm(Av)

        if np.allclose(v, new_v, rtol=tolerance):
            break

        v = new_v

    return eigenvalue, v


A = np.array([[4, 1, 1], [1, 3, -1], [1, -1, 2]])

eigenvalue, eigenvector = power_iteration(A)
print("Dominant eigenvalue:", eigenvalue)
print("Corresponding eigenvector:", eigenvector)


# Q j-2
def qr_algorithm(A, num_iterations=1000):
    n = A.shape[0]
    Q = np.eye(n)

    for _ in range(num_iterations):
        Q_k, R_k = np.linalg.qr(A)
        A = R_k @ Q_k
        Q = Q @ Q_k

    eigenvalues = np.diag(A)
    eigenvectors = Q

    return eigenvalues, eigenvectors


A = np.array([[4, 1, 1], [1, 3, -1], [1, -1, 2]])

eigenvalues, eigenvectors = qr_algorithm(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
