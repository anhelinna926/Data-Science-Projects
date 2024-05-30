# Import required libraries
import numpy as np

array_2d = [[5, 10, 15, 20], [25, 30, 35, 40], [45, 50, 55, 60]]

# TODO: Create a 2D numpy array
np_array_2d = np.array(array_2d)
# TODO: Print the details of the array (dimensions, shape, size, and datatype)
print(")Dimensions: ", np_array_2d.ndim)
print("Shape: ", np_array_2d.shape)
print("Size: ", np_array_2d.size)
print("Data type", np_array_2d.dtype)
# TODO: Perform indexing and slicing operations to access specific elements and slices of the array
element = np_array_2d[0, 0]
print("Element at first row, first column:", element)
first_row = np_array_2d[0, :]
print("First row:", first_row)
# TODO: Reshape the array to a different size with the same number of elements. Don't forget to print the reshaped array!2d
# Reshape the array to 4 rows and 3 columns
reshaped_array = np_array_2d.reshape(4, 3)
# Print the reshaped array
print("Reshaped array:\n", reshaped_array)
