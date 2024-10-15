from random import randint
from typing import List


def get_matrix_from_user(rows: int, columns: int) -> List[List[int]]:
    """
    Запрашивает у пользователя значения для заполнения матрицы.

    Args:
        rows (int): Количество строк в матрице.
        columns (int): Количество столбцов в матрице.

    Returns:
        List[List[int]]: Матрица, заполненная пользовательскими значениями.
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    value = int(input(f"Введите значение для элемента [{i + 1}][{j + 1}]: "))
                    row.append(value)
                    break
                except ValueError:
                    print("Ошибка: Введите целое число.")
        matrix.append(row)
    return matrix


def generate_matrix(rows: int, columns: int) -> List[List[int]]:
    """
    Генерирует матрицу со случайными значениями.

    Args:
        rows (int): Количество строк в матрице.
        columns (int): Количество столбцов в матрице.

    Returns:
        List[List[int]]: Матрица, заполненная случайными значениями от 0 до 100.
    """
    return [[randint(0, 100) for _ in range(columns)] for _ in range(rows)]


def generate_or_input(rows: int, columns: int) -> List[List[int]]:
    """
    Предлагает пользователю выбрать способ заполнения матрицы: вручную или автоматически.

    Args:
        rows (int): Количество строк в матрице.
        columns (int): Количество столбцов в матрице.

    Returns:
        List[List[int]]: Матрица, заполненная в соответствии с выбором пользователя.
    """
    choice = input("Введите число:\n\t1 - заполнение данных самому\n\t2 - генерация данных")
    match choice:
        case "1":
            return get_matrix_from_user(rows, columns)
        case "2":
            return generate_matrix(rows, columns)
        case _:
            generate_or_input()


def user_input() -> List[List[int]]:
    """
    Запрашивает у пользователя размеры матрицы и вызывает функцию для её заполнения.

    Returns:
        List[List[int]]: Матрица, заполненная в соответствии с выбором пользователя.
    """
    while True:
        try:
            rows = int(input("Введите размер списка:\t"))
            columns = int(input("Введите размер подсписков:\t"))
            break
        except ValueError:
            print("Вводите только числа!")
    return generate_or_input(rows, columns)
