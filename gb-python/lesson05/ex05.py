# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summ():
    try:
        with open('ex05.txt', 'w+') as file1:
            line = input('Введи числа через пробел \n')
            file1.writelines(line)
            numbers = line.split()

            print(f'Сумма введённых чисел:', sum(map(int, numbers)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Введено что-то неправильное. Ошибка ввода-вывода')


summ()
