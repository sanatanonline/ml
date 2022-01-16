import numpy as np
from numpy import array
from numpy import mean
from numpy.linalg import eig

C_1 = array([[1, 2], [2, 3], [3, 3], [4, 5], [5, 5]])
C_2 = array([[1, 0], [2, 1], [3, 1], [3, 2], [5, 3], [6, 5]])
print("We have the data:")
print("Class C1:\n", C_1)
print("Class C1:\n", C_2)
M_1 = mean(C_1.T, axis=1)
M_2 = mean(C_2.T, axis=1)
print("Step1: Let's compute the mean for each class:")
print("Mean of class C1: mu1 = \n", M_1)
print("Mean of class C2: mu2 = \n", M_2)
S_1 = (len(C_1) - 1) * np.cov(C_1.T)
S_2 = (len(C_2) - 1) * np.cov(C_2.T)
print("Step2: Let's compute the scatter matrices for each class:")
print("Scatter matrix of class C1: S1 = \n", S_1)
print("Scatter matrix of class C2: S2 = \n", S_2)
S_W = S_1 + S_2
print("Step3: Within the class scatter S_W = S_1 + S_2")
print("S_W = \n", S_W)
S_W_I = np.linalg.inv(S_W)
print("Step4: Let's compute the inverse of S_W")
print("S_W_I = \n", S_W_I)
V = np.matmul(S_W_I, (M_1 - M_2))
print("Step5: The optimal line direction v = S_W_I(mu1-mu2)")
print("v = \n", V)
