# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

print('Параметры настраиваются: правой кнопкой - Edit Run Configuration - Parameters')

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    result = time * salary + bonus
    print(f'ЗП сотрудника {result}')
except ValueError:
    print('Не число')
