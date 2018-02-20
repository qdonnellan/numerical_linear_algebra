import numpy as np

x = np.array([[0.85, 0.10, 0.05, 0]])

A = np.array([
    [0.90, 0.07, 0.02, 0.01],
    [0.00, 0.93, 0.05, 0.02],
    [0.00, 0.00, 0.85, 0.15],
    [0.00, 0.00, 0.00, 1.00]
])

after_one_year = np.dot(A.T, x.T)

print(after_one_year)
