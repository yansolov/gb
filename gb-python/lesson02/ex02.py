element_count = int(input("Введи количество элементов списка "))
list1 = []
i = 0
element = 0
while i < element_count:
    list1.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(list1)/2)):
        list1[element], list1[element + 1] = list1 [element + 1], list1[element]
        element += 2
print(list1)

# el_count = int(input("Введите количество элементов списка "))
# my_list = []
# i = 0
# el = 0
# while i < el_count:
#     my_list.append(input("Введите следующее значение списка "))
#     i += 1
#
# for elem in range(int(len(my_list)/2)):
#         my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
#         el += 2
# print(my_list)