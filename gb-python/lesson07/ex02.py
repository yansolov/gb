# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
# обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Odezhda:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def palto_square(self):
        return self.width / 6.5 + 0.5

    def kostume_square(self):
        return self.height * 2 + 0.3

    @property
    def square_all(self):
        return str(f'Общая площадь ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Palto(Odezhda):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_p = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто {self.square_p}'


class Kostume(Odezhda):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_k = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм {self.square_k}'


palto = Palto(2, 4)
kostume = Kostume(1, 2)
print(palto)
print(kostume)
print(palto.square_all)
print(kostume.square_all)
print(kostume.palto_square())
print(kostume.kostume_square())
