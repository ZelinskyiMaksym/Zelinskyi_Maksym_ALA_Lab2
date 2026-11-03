import numpy as np


def generate_random_square_matrix(n):
    return np.random.randint(0, 256, (n, n))