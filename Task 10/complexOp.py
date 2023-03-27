import numpy as np

my_array = np.array([0, np.pi/4, np.pi/2])

# Trigonometric functions
# Sine function
print(np.sin(my_array))  # Output: [0. 0.70710678 1.]

# Cosine function
print(np.cos(my_array))  # Output: [1.000000e+00 7.071068e-01 6.123234e-17]

# Tangent function
print(np.tan(my_array))  # Output: [0.00000000e+00 1.00000000e+00 1.63312394e+16]


# -------------------------------------------------------

# Exponential and logarithmic functions
my_array = np.array([1, 2, 3])

# Exponential function
print(np.exp(my_array))  # Output: [ 2.71828183  7.3890561  20.08553692]

# Natural logarithm function
print(np.log(my_array))  # Output: [0. 0.69314718 1.09861229]

# Base-10 logarithm function
print(np.log10(my_array))  # Output: [0. 0.30103    0.47712125]

# Base-2 logarithm function
print(np.log2(my_array))  # Output: [0. 1. 1.5849625]

# -------------------------------------------------------

# Matrix operations
# Create two NumPy arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Dot product
print(np.dot(a, b))  # Output: [[19 22]
                     #          [43 50]]

# Transpose
print(a.T)  # Output: [[1 3]
            #          [2 4]]

# Eigenvalues and eigenvectors
eigvals, eigvecs = np.linalg.eig(a)
print(eigvals)  # Output: [-0.37228132  5.37228132]
print(eigvecs)  #[[-0.82456484 -0.41597356]
                # [ 0.56576746 -0.90937671]]

