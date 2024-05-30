import numpy as np

# Initializing two 3x3 matrices using numpy array
matrix_A = np.array([[3, 3, 4], [5, 6, 7], [8, 9, 10]])
matrix_B = np.array([[12, 13, 14], [14, 16, 17], [19, 20, 21]])

# TODO: Normalize matrix_A in the range [0,1] using min-max normalization
norm_matrix_A = (matrix_A - np.min(matrix_A)) / (np.max(matrix_A) - np.min(matrix_A))
print("Normilized Matrix A:\n", norm_matrix_A)
# TODO: Take the transpose of the normalized matrix_A
transposed_matrix = norm_matrix_A.T
print("Transposwd Matrix A:\n", transposed_matrix)
# Assume these are the weights for features in matrix_A
weights = np.array([0.3, 0.5, 0.2])

# TODO: Compute the dot product of the transposed normalized matrix and weights
weighted_sum = np.dot(transposed_matrix, weights)
print("Weighted Sum:\n", weighted_sum)
# TODO: Calculate the inverse matrix for `matrix_A` and calculate their product - it should result in the identity matrix
inversed_matrix_A = np.linalg.inv(matrix_A)
identity_result = np.dot(matrix_A, inversed_matrix_A)
print("Identity Result:", identity_result)