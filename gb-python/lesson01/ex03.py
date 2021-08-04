m = int(input("Введи число n от 0 до 9: "))

n = str(m)
nn = n + n
nnn = n + n + n

summa = m + int(nn) + int(nnn)

print("Сумма n + nn + nnn = {} + {} + {} = {}".format(m, nn, nnn, summa))