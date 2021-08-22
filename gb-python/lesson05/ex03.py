# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
# сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('ex03.txt', 'r', encoding='utf-8') as my_file:
    salary = []
    lowsalary = []
    my_list = my_file.read().split('\n')

    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           lowsalary.append(i[0])
        salary.append(i[1])
print(f'ЗП меньше 20.000 {lowsalary}, \nсредний оклад {sum(map(int, salary)) / len(salary)}')
