import numpy as np

# Create sample arrays for linear algebra operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)
print("Matrix multiplication of A and B:\n", C)
# Output: [[19 22]
#          [43 50]]

# Matrix transpose
D = np.transpose(A)
print("Transpose of A:\n", D)
# Output: [[1 3]
#          [2 4]]

# Inverse of a matrix
E = np.linalg.inv(A)
print("Inverse of A:\n", E)
# Output: [[-2.   1. ]
#          [ 1.5 -0.5]]

# Rank of a matrix
rank_A = np.linalg.matrix_rank(A)
print("Rank of A:", rank_A)
# Output: 2

# Complex Operations
# Sample Arrays
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])

# Determinant of a matrix
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)
# Output: 0.0

# Eigenvalues and eigenvectors of a matrix
eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues of A:", eigvals)
# Output: array([ 1.61168440e+01, -1.11684397e+00, -9.75918483e-16])
print("Eigenvectors of A:\n", eigvecs)
# Output: array([[-0.23197069, -0.78583024,  0.40824829],
#                [-0.52532209, -0.08675134, -0.81649658],
#                [-0.8186735 ,  0.61232756,  0.40824829]])

# Singular value decomposition
U, S, V = np.linalg.svd(A)
print("Singular values of A:", S)
# Output: array([1.68481034e+01, 1.06836951e+00, 3.33475287e-16])

# Create a random vector
v = np.random.rand(3)

# Projection of a vector onto a subspace spanned by a matrix
P = np.dot(A, np.dot(np.linalg.inv(np.dot(A.T, A)), A.T))
proj_v = np.dot(P, v)
print("Projection of v onto subspace spanned by A:\n", proj_v)
# Output: an array of length 3 containing the coordinates of the projection of v onto the subspace spanned by A. The exact values depend on the randomly generated vector v.
