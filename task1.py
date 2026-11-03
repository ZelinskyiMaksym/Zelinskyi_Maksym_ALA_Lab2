import eigenvalues_eigenvectors as eva_eve
import matrix_generator as mg


def run_task1():
    print("\nЗадача 1")
    matrix = mg.generate_random_square_matrix(int(input("Введіть розмір бажаної квадратної матриці: ")))
    eigenvalues, eigenvectors = eva_eve.get_eigenvalues_and_eigenvectors(matrix)

    print("Наша квадратна матриця:\n", matrix,
          "\nВласні значення:\n", eigenvalues,
          "\nВласні вектори:\n", eigenvectors)
    print("Завершено виконання: Задача 1\n")





