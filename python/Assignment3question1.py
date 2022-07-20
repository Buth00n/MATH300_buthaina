

import numpy as np

# creating the array "a"
A = np.array([[1, 2], [3, 4]])
B = np.array([5, 8])
print("Array A is: \n", A)
print("Array B is : \n", B)

# Calculating the equation
x = np.linalg.solve(A, B)

# Printing the answer
print("The value for x is  :\n", x)
