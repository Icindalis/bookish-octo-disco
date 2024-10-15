def function3():
    n = int(input("Введите количество подсписков: "))
    nested_list = []

    for i in range(n):
        sub_len = int(input(f"Введите количество элементов в подсписке {i+1}: "))
        sublist = []
        for j in range(sub_len):
            value = int(input(f"Введите элемент {j+1} подсписка {i+1}: "))
            sublist.append(value)
        nested_list.append(sublist)

    nested_list.sort(key=sum)

    print("Отсортированный вложенный список:")
    for sublist in nested_list:
        print(sublist)

if __name__ == "3":
    function3()

def function3():
    nested_list.sort(key=sum)

if __name__ == "3":
    function3()