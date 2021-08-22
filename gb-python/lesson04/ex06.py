# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle


def count_func(start, stop):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


def repeat_func(my_list, iteration):
    i = 0
    num = cycle(my_list)
    while i < iteration:
        print(next(num))
        i += 1


count_func(start=int(input("Введи стартовое число: ")), stop=int(input("Введи последнее число: ")))
repeat_func(my_list=[10, -20, None, 'text'], iteration=int(input("Введи количество итераций: ")))
