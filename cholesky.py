import numpy as np


# Check if a matrix is positive definite by verifying if all eigenvalues are greater than zero
def is_positive_definite(A):
    eigenvalues = np.linalg.eigvals(A)
    return np.all(eigenvalues > 0)


# Perform Cholesky decomposition on a positive definite matrix
def cholesky_decomposition(A):
    if not is_positive_definite(A):
        raise ValueError("Matrix is not positive definite.")

    n = len(A)
    L = np.zeros_like(A, dtype=float)

    for i in range(n):
        for j in range(i + 1):
            # Calculate the sum of squares of the already computed elements
            s = sum(L[i, k] * L[j, k] for k in range(j))
            if i == j:
                L[i, j] = np.sqrt(A[i, j] - s)
            else:
                L[i, j] = (A[i, j] - s) / L[j, j]

    return L


# Solve the system of equations Ax = b using Cholesky decomposition
def solve_cholesky(L, b):
    n = len(L)
    y = np.zeros_like(b, dtype=float)
    x = np.zeros_like(b, dtype=float)

    # Forward substitution: Solve Ly = b
    for i in range(n):
        s = sum(L[i, j] * y[j] for j in range(i))
        y[i] = (b[i] - s) / L[i, i]

    # Back substitution: Solve L.T x = y
    for i in range(n - 1, -1, -1):
        s = sum(L[j, i] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - s) / L[i, i]

    return x


# Input matrix A from user
rows = int(input("Enter the number of rows for matrix A: "))
cols = int(input("Enter the number of columns for matrix A: "))
A = np.zeros((rows, cols))
print("Enter the elements of matrix A:")

for i in range(rows):
    for j in range(cols):
        A[i, j] = float(input(f"A[{i}, {j}]: "))

# Input vector b from user
n = int(input("Enter the size of vector b: "))
b = np.zeros(n)
print("Enter the elements of vector b:")

for i in range(n):
    b[i] = float(input(f"b[{i}]: "))

# Check if the matrix is positive definite
if is_positive_definite(A):
    # Perform Cholesky decomposition
    L = cholesky_decomposition(A)

    # Solve the system of equations using Cholesky decomposition
    x = solve_cholesky(L, b)

    # Print the Cholesky decomposition matrix
    print("Cholesky Decomposition:")
    print(L)

    # Print the solution vector
    print("\nSolution x:")
    print(x)
else:
    print("Matrix is not positive definite.")
