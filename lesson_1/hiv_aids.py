import numpy as np

current_states = np.array([0.85, 0.10, 0.05, 0])

stochastic_matrix = np.array([
    [0.90, 0.07, 0.02, 0.01],
    [0.00, 0.93, 0.05, 0.02],
    [0.00, 0.00, 0.85, 0.15],
    [0.00, 0.00, 0.00, 1.00]
])

after_one_year = np.dot(current_states, stochastic_matrix)

print(after_one_year)
