firstkm = int(input("Спортсмен пробежал в первый день, км: "))
lastkm = int(input("В последний день он пробежал не менее, км: "))
day = 1

while firstkm <= lastkm:
    firstkm = firstkm * 1.1
    day += 1

print("Номер дня: ", day)
