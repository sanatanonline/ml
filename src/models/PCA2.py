import numpy as np
from numpy import array
from numpy import mean
from numpy.linalg import eig

D = array([[4, -1], [-2, 3]])
print("We have the data: \n D=")
print(D)
MU = mean(D.T, axis=1)
print("Step1: Compute the mean vector: \n mu =")
print(MU)
Z = D - MU
print("Step2: Subtract the mean from data: Z = X - MU \n Z =")
print(Z)
S = len(Z) * np.cov(Z.T)
print("Step3: Calculate the scatter matrix: \n S =")
print(S)
values, vectors = eig(S)
print("Step4: Compute the eigen vectors and eigen values.")
print("Eigen vectors (e_i):")
print(vectors)
print("Eigen values (lambda_i:")
print(values)
P = vectors.T.dot(Z.T)
print("Step5: Projected Data:")
print(P.T)
