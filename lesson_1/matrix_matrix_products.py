import numpy as np


D = np.array([
    [6, 5, 3, 1],
    [3, 6, 2, 2],
    [3, 4, 3, 1]
])

cost = np.array([
    [1.5, 1.0],
    [2.0, 2.5],
    [5.0, 4.5],
    [16.0, 17.0]
])

ans = np.dot(D, cost)

print(ans)
