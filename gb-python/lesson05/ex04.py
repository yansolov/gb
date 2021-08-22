# Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.


translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('ex04.txt', 'r') as file1:
    for i in file1:
        i = i.split(' ', 1)
        new_file.append(translate[i[0]] + ' ' + i[1])
    print(new_file)

with open('ex04.txt', 'w') as file2:
    file2.writelines(new_file)
