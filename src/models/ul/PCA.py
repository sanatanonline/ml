from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig
import pandas as pd

# define a matrix
A = array([[1, 2], [2, 3], [3, 2], [4, 4], [5, 4], [6, 7], [7, 6], [9, 7]])

print("We have the data:")
print(A)
# calculate the mean of each column
M = mean(A.T, axis=1)
print("Step1: Let's compute the mean vector:")
print(M)
# center columns by subtracting column means
C = A - M
print("Step2: Subtract the mean from data:")
print(C)
# calculate covariance matrix of centered matrix
V = cov(C.T)
print("Step3: Let's calculate the covariance matrix:")
print(V)
# eigendecomposition of covariance matrix
values, vectors = eig(V)
print("Step4: Let's calculate the eigen vectors and eigen values.")
print("Eigen vectors:")
print(vectors)
print("Eigen values:")
print(values)

# project data
P = vectors.T.dot(C.T)
print("Step5: Projected Data:")
print(P.T)
