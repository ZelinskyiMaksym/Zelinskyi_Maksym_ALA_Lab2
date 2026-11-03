import numpy as np
from image_loader import get_black_white_image as get_bw_image
from visualization import show_cumulative_variance


def compress_image(path, quality=0.95, show_cum_var=False):
    image = get_bw_image(path)
    image_mean = np.mean(image, axis=0)

    mean_matrix = image - image_mean
    covariance_matrix = np.cov(mean_matrix, rowvar=False)
    covariances_eigenvalues, covariances_eigenvectors = np.linalg.eigh(covariance_matrix)

    sorted_indexes = np.argsort(-covariances_eigenvalues)
    covariances_eigenvalues = covariances_eigenvalues[sorted_indexes]
    covariances_eigenvectors = covariances_eigenvectors[:, sorted_indexes]

    total_variance = covariances_eigenvalues.sum()
    if total_variance <= 0:
        raise ValueError("Загальна дисперсія дорівнює нулю")

    cumulative_variance = (np.cumsum(covariances_eigenvalues) / total_variance)

    n_components = 0
    for fraction in cumulative_variance:
        n_components += 1
        if fraction >= quality:
            print("Кількість власних векторів, використаних для стиснення: ", n_components, "з", len(cumulative_variance))
            if show_cum_var:
                show_cumulative_variance(range(1, len(cumulative_variance) + 1), cumulative_variance * 100, n_components, quality)
            break

    matrix_of_selected_eigenvectors = covariances_eigenvectors[:, :n_components]
    compressed_image = mean_matrix @ matrix_of_selected_eigenvectors

    return compressed_image, image_mean, matrix_of_selected_eigenvectors


def image_decompression(compressed_image, image_mean, matrix_of_selected_eigenvectors):
    image = (compressed_image @ matrix_of_selected_eigenvectors.T) + image_mean

    return image
