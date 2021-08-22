# Представлен список чисел. Необходимо вывести элементы исходного
# списка, значения которых больше предыдущего элемента.

list1 = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 5]
list2 = [element for element in list1 if element > list1[list1.index(element) - 1]]

print(f'Изначальный список {list1}')
print(f'Новый список {list2}')
