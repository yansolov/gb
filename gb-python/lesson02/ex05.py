number = int(input("Введи число: "))
my_list = [7, 5, 3, 3, 2]
count = my_list.count(number)
for element in my_list:
    if count > 0:
        i = my_list.index(number)
        my_list.insert(i+count, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list) 