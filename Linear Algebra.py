# Linear Algebra
import numpy as np
A = np.array([[4,3],[-5,9]])
B = np.array([20,26])
X = np.linalg.inv(A).dot(B)
Y = np.linalg.solve(A,B)
print(X)
print(Y)

# Rank np.linalg.matrix_rank(A)
# Trace np.trace(A)
# Determinant np.linalg.det(A)
# Inverse np.linalg.inv(A)
# Power np.linalg.matrix_power(A,B)

# Eigh Function
a = np.array([[1,-2j],[2j,5]])
print("Array is: ",a)
c,d = np.linalg.eigh(a)
print("Eigh values: ",c)
print("Eigh vectors: ",d)

# for just values for normal matrix - np.linalg.eigvals(a)
# for just values for complex matrix - np.linalg.eigvalsh(a)

# Ravel Function changes 2D or MultiD array to flattened array
x = np.array([[1,3,5],[11,56,35]])
y = np.ravel(x)
print(y)

# Scipy same as numpy
import scipy
import numpy as np
A = np.array([[4,3],[-5,9]])
B = np.array([20,26])
X = scipy.linalg.inv(A).dot(B)
Y = scipy.linalg.solve(A,B)
print(X)
print(Y)



# Q1)
import numpy as np
A = np.array([[4,3,2],[-2,2,3],[3,-5,2]])
B = np.array([25,-10,-4])
X = np.linalg.inv(A).dot(B)
print(X)

# Q2)
import numpy as np

def calculate(a):
    rank = np.linalg.matrix_rank(a)
    determinant = np.linalg.det(a)
    inverse = np.linalg.inv(a)
    return rank,determinant,inverse

a = np.array([[4,3,2],[-2,2,3],[3,-5,2]])
rank,determinant,inverse = calculate(a)
print("Rank: ",rank)
print("Determinant: ",determinant)
print("Inverse: ",inverse)
