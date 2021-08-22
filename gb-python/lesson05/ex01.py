#  Создать программно файл в текстовом формате, записать в него построчно данные,
#  вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_file = open('ex01.txt', 'w')
line = input('Введи текст \n')
while line:
    my_file.writelines(line)
    line = input('Введи текст \n')
    if not line:
        break

my_file.close()
my_file = open('ex01.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()