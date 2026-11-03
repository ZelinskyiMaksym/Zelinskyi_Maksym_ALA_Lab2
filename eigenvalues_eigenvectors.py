import numpy as np


def get_eigenvalues_and_eigenvectors(A):
    A = np.array(A)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("Матриця не квадратна")

    values, vectors = np.linalg.eig(A)
    n = A.shape[0]

    # Перевірка результату
    for indx in range(n):
        value = values[indx]
        vector = vectors[:, indx]

        left = A @ vector
        right = value * vector

        if not np.allclose(left, right):
            raise ValueError(f"Пара власного вектора і власного значення під номером {indx + 1} не пройшла перевірку")

    # Перетворення власних значень із нульовою уявною частиною
    converted_values = []

    for value in values:
        if np.imag(value) == 0:
            converted_values.append(np.real(value))
        else:
            converted_values.append(value)

    return converted_values, vectors
