from matrix import user_input
from min_last_element_sublist import find_sublist_with_min_last_element
from task3 import sort_subs

def main():
    # user_input возвращает список с вложенными списками
    matrix = user_input()
    # 2
    print(find_sublist_with_min_last_element(matrix))
    # 3
    print(sort_subs(matrix))

if __name__ == '__main__':
    main()
