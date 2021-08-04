n = int(input("Введи целое положительное число: "))

maks = 0
while n > 0:
    c = n % 10
    if c >= maks:
        maks = c
    n = n // 10

print("Самая большая цифра в числе:", maks)
