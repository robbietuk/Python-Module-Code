import numpy as np

# Constants
bird_count = 10

# setup box
limits = np.array([2000, 2000])

position = np.random.rand(2, bird_count) * limits[:, np.newaxis]

