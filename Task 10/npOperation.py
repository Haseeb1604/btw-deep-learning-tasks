import numpy as np

# Create a 1D array
my_array = np.array([1, 2, 3, 4, 5])

# Indexing
print(my_array[0])  # Output: 1

# Slicing
print(my_array[1:4])  # Output: [2 3 4]

# Math Operation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Addition
c = a + b
print(c)  # Output: [5 7 9]

# Subtraction
c = b - a
print(c)  # Output: [3 3 3]

# Multiplication
c = a * b
print(c)  # Output: [ 4 10 18]

# Division
c = b / a
print(c)  # Output: [4.  2.5 2. ]

# Aggregation operations

# Sum
print(np.sum(my_array))  # Output: 15

# Minimum
print(np.min(my_array))  # Output: 1

# Maximum
print(np.max(my_array))  # Output: 5

# Mean
print(np.mean(my_array))  # Output: 3.0

# Standard deviation
print(np.std(my_array))  # Output: 1.4142135623730951

# Boolean operations
print(my_array > 2)  # Output: [False False  True  True  True]
print(my_array < 4)  # Output: [ True  True  True False False]
print((my_array > 2) & (my_array < 4))  # Output: [False False  True False False]
print((my_array > 2) | (my_array < 4))  # Output: [ True  True  True  True  True]
print(~(my_array > 2))  # Output: [ True  True False False False]
