import numpy as np

# Create a 2D array
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Indexing
print(my_array[0, 0])  # Output: 1
print(my_array[1, 2])  # Output: 6

# Slicing
print(my_array[0:2, 1:3])  # Output: [[2 3]
                          #          [5 6]]

# Create two 2D arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Element-wise addition
c = a + b
print(c)  # Output: [[ 6  8]
          #          [10 12]]

# Element-wise subtraction
c = a - b
print(c)  # Output: [[-4 -4]
          #          [-4 -4]]

# Element-wise multiplication
c = a * b
print(c)  # Output: [[ 5 12]
          #          [21 32]]

# Element-wise division
c = b / a
print(c)  # Output: [[5.         3.        ]
          #          [2.33333333 2.        ]]

# Matrix multiplication
c = np.dot(a, b)
print(c)  # Output: [[19 22]
          #          [43 50]]

# Aggregation operations
# Sum
print(np.sum(my_array))  # Output: 45
# Sum of rows
print(np.sum(my_array, axis=0))  # Output: [12 15 18]
# Sum of columns
print(np.sum(my_array, axis=1))  # Output: [ 6 15 24]
# Minimum
print(np.min(my_array))  # Output: 1
# Maximum
print(np.max(my_array))  # Output: 9
# Mean
print(np.mean(my_array))  # Output: 5.0
# Standard deviation
print(np.std(my_array))  # Output: 2.581988897471611

# Boolean operations 
# Boolean indexing
bool_array = my_array > 5
print(bool_array)  # Output: [[False False False]
                   #          [False False  True]
                   #          [ True  True  True]]
print(my_array[bool_array])  # Output: [6 7 8 9]

# Boolean operations
bool_array1 = my_array > 3
bool_array2 = my_array < 8
print(bool_array1)  # Output: [[False False False]
                    #          [ True  True  True]
                    #          [ True  True  True]]
print(bool_array2)  # Output: [[ True  True  True]
                    #          [ True  True  True]
                    #          [ True False False]]
print(np.logical_and(bool_array1, bool_array2))  # Output: [[False False False]
                                                 #          [ True  True  True]
                                                 #          [ True False False]]
print(np.logical_or(bool_array1, bool_array2))  # Output: [[ True  True  True]
                                                #          [ True  True  True]
                                                #          [ True  True  True]]
print(np.logical_not(bool_array1))  # Output: [[ True  True  True]
                                     #          [False False False]
                                     #          [False False False]]
                                     
# Transpose
# Transpose using the .T attribute
transposed_array1 = my_array.T
print(transposed_array1)  # Output: [[1 4 7]
                          #          [2 5 8]
                          #          [3 6 9]]

# Transpose using the transpose() function
transposed_array2 = np.transpose(my_array)
print(transposed_array2)  # Output: [[1 4 7]
                          #          [2 5 8]
                          #          [3 6 9]]