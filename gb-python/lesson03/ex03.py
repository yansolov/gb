# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(ar1, ar2, ar3):
    massive = [ar1, ar2, ar3]
    summa = []
    max1 = max(massive)
    summa.append(max1)
    massive.remove(max1)
    max2 = max(massive)
    summa.append(max2)
    print(sum(summa))


my_func(int(input("Введи первое число = ")), int(input("Введи второе число = ")),
        int(input("Введи третье число = ")))
