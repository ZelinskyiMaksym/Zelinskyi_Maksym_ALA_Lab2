import numpy as np
import matrix_generator as mg


def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))

    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector


def decrypt_message(encrypted_vector, key_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    decrypted_matrix = np.dot(np.dot(eigenvectors, np.linalg.inv(np.diag(eigenvalues))), np.linalg.inv(eigenvectors))
    decrypted_message_vector = np.dot(decrypted_matrix, encrypted_vector)

    codes = np.rint(decrypted_message_vector.real)
    message = "".join(chr(int(code)) for code in codes)

    return message


def generate_key_matrix(message):
    random_matrix = mg.generate_random_square_matrix(len(message))
    key_matrix = np.dot(random_matrix.T, random_matrix) + np.eye(len(message))
    return key_matrix
