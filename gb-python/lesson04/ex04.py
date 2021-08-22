# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести
# в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list2 = [element for element in list1 if list1.count(element) == 1]

print(f'Изначальный список {list1}')
print(f'Новый список {list2}')
