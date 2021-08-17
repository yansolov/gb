# Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные
# аргументы. Реализовать вывод данных о пользователе одной строкой.

def func2(name, surname, year, city, email, tel):
    print(name, surname, year, city, email, tel)


# name = input("Введи имя")
# surname = input("Введи фамилию")
# year = int(input("Введи год рождения"))
# city = input("Введи город")
# email = input("Введи email")
# tel = input("Введи телефон")

func2(name="John", surname="Smith", year=1991, city="Moscow", email="gb@gb.ru", tel="1234")
