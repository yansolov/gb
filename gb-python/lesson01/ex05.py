income = int(input("Введи выручку, руб: "))
costs = int(input("Введи издержки, руб: "))

profit = income - costs

if profit > 0:
    profitability = round(profit / income * 100,1)
    print("Фирма работает с прибылью {} рублей, рентабельность {}%".format(profit, profitability))

    stuff = int(input("Введи численность сотрудников: "))
    parameter = round(profit/stuff,1)
    print("Прибыль на одного сотрудника составляет {} руб".format(parameter))

else:
    print(("Фирма работает в убыток: {} руб".format(profit)))