# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def func1(first, second):
    try:
        division = first / second
        return division
    except ZeroDivisionError:
        return "Второе число не должно быть 0"
    except ValueError:
        return "Вводи только числа"


print(func1(int(input("Введи первое число = ")), int(input("Введи второе число = "))))
