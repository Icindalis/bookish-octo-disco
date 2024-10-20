from matrix import user_input
from min_last_element_sublist import find_sublist_with_min_last_element


def main():
    # user_input возвращает список с вложенными списками
    matrix = user_input()
    # 2
    print(find_sublist_with_min_last_element(matrix))

if __name__ == '__main__':
    main()
