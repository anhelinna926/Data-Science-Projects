import numpy as np

# Create a 3x3 matrix using `np.random.randint`
matrix_a = np.random.randint(255, size=(3, 3))
print("Matrix A:\n", matrix_a)

# TODO: Normalize Matrix A between 0 and 1.
norm_matrix_a =( matrix_a - np.min(matrix_a)) / (np.max(matrix_a) - np.min(matrix_a))
# TODO: Find the transpose of the normalized matrix.
print("Normilized Matrix A:\n", norm_matrix_a)
transposed_matrix = norm_matrix_a.T
print("Transposed Numeric Matrix:\n", transposed_matrix)