from typing import List


def find_sublist_with_min_last_element(matrix: List[list[int]]) -> list[int]:
    """
        Находит подсписок с минимальным последним элементом.

        Функция принимает матрицу (список списков целых чисел) и возвращает подсписок,
        у которого последний элемент является наименьшим среди всех последних элементов подсписков.

        Args:
            matrix (List[list[int]]): Матрица, представленная как список списков целых чисел.

        Returns:
            list[int]: Подсписок с минимальным последним элементом.

        Raises:
            IndexError: Если один из подсписков пуст или матрица пуста.

        Example:
            >>> matrix = [[3, 5], [2, 8], [1, 4]]
            >>> find_sublist_with_min_last_element(matrix)
            [1, 4]
        """
    if not matrix or any(len(sublist) == 0 for sublist in matrix):
        msg = "Матрица пуста или один из подсписков пуст."
        raise IndexError(msg)
    min_last_element = matrix[0][-1]
    min_sublist = matrix[0]
    for i in matrix:
        if i[-1] < min_last_element:
            min_last_element = i[-1]
            min_sublist = i
    return min_sublist