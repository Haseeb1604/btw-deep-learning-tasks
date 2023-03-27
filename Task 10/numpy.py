# Numpy
# Numpy arrays are like list in python but more efficient for numerical analysis since they are implemented in C

# Importing Numpy
import numpy as np

# Create a NumPy array from a list
# 1D Array
my_list = [1, 2, 3, 4, 5, 6]

my_array = np.array(my_list)

print(my_array) # Output: [1 2 3 4 5 6]
print(type(my_array)) # Output: <class 'numpy.ndarray'>

# Reshape the array into a 2D array with 2 rows and 3 columns
a = my_array.reshape(2, 3)
print(a)  # Output: [[1 2 3]
           #          [4 5 6]]

# Flatten the 2D array back into a 1D array
b = my_array.flatten()
print(b)  # Output: [1 2 3 4 5 6]


# 2D array from a nested list
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

my_array = np.array(my_list)
print(my_array)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]
#  [10 11 12]]

# Reshape the array to have 2 rows and 6 columns
a = my_array.reshape(2, 6)
print(a)
# Output:
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]

# Reshape the array to have 6 rows and 2 columns
b = my_array.reshape(6, 2)
print(b)
# Output:
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]
#  [11 12]]

# 3D array from a nested list
my_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

my_array = np.array(my_list)
print(my_array)
# Output:
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]

# Reshape the array to have 4 rows and 2 columns
a = my_array.reshape(4, 2)
print(a)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Reshape the array to have 2 rows, 2 columns, and 2 layers
b = my_array.reshape(2, 2, 2)
print(b)
# Output:
# [[[1 2]
#   [3 4]]
# 
#  [[5 6]
#   [7 8]]]

# -----------------------------------------------
# Stack
# Create two 1D NumPy arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack the two arrays vertically
c = np.vstack((a, b))
print(c)  # Output: [[1 2 3]
           #          [4 5 6]]

# Stack the two arrays horizontally
d = np.hstack((a, b))
print(d)  # Output: [1 2 3 4 5 6]

# Concatenate the two arrays along a new axis
e = np.concatenate((a[:, np.newaxis], b[:, np.newaxis]), axis=1)
print(e)  # Output: [[1 4]
           #          [2 5]
           #          [3 6]]