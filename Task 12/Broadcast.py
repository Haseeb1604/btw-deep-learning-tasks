# Broadcasting allows numpy to work with arrays of different shapes and sizes. 
# The rules of broadcasting are as follows:
#  - If the arrays do not have the same number of dimensions, numpy will prepend the smaller array with ones until they have the same number of dimensions.
#  - If the sizes of the corresponding dimensions are not equal, numpy will stretch the smaller array along that dimension until it has the same size as the larger array.

import numpy as np

# Create a 2D array and manipulating with 1D Array
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

# Create a 1D array
arr2 = np.array([10, 20, 30])

# Add the arrays together
result = arr1 + arr2

# Print the result
print(result)

# Output
# [[11 22 33]
#  [14 25 36]]

# Now using 3D Arrays with 1D Array
arr1 = np.array([[[1, 2], [3, 4], [5, 6]],
                 [[7, 8], [9, 10], [11, 12]]])

# 1D Array
arr2 = np.array([10, 20])

# Multiply the arrays together
result = arr1 * arr2

# Print the result
print(result)
# Ouput
# [[[ 10  40]
#   [ 30  80]
#   [ 50 120]]

#  [[ 70 160]
#   [ 90 200]
#   [110 240]]]

# 2D Array with 3D Array
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

# 3D Array
arr2 = np.array([[[10], [20], [30]], [[40], [50], [60]]])

# Add the arrays together
result = arr1 + arr2

# Print the result
print(result)
# [[[11 12 13]
#   [24 25 26]
#   [35 36 37]]

#  [[41 42 43]
#   [54 55 56]
#   [65 66 67]]]
