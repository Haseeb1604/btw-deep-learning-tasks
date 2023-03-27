# Numpy
# Numpy arrays are like list in python but more efficient for numerical analysis since they are implemented in C

# Importing Numpy
import numpy as np

# Create a NumPy array from a list
# 1D Array
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array) # Output: [1 2 3 4 5]
print(type(my_array)) # Output: <class 'numpy.ndarray'>

# 2D array from a nested list
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_array = np.array(my_list)
print(my_array)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 3D array from a nested list
my_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
my_array = np.array(my_list)
print(my_array)
# Output:
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]
