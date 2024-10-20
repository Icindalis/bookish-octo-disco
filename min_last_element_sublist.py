from typing import List


def find_sublist_with_min_last_element(matrix: List[list[int]]) -> list[int]:
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