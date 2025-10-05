from math import gcd as gsd


class FractionPart:
    def __init__(self, first: int = 0, second: int = 1):
        if second == 0:
            raise ValueError("Знаменатель не может быть 0")

        self.__first = int(abs(first))
        self.__second = int(abs(second))

        self.normalize()

    def read(self):
        self.__first = int(input("Введите числитель: "))
        self.__second = int(input("Введите знаменатель: "))

        if self.__second == 0:
            raise ValueError("Знаменатель не может быть 0")

    def display(self):
        print(f"{self.__first}/{self.__second}")
        print(f"Целая часть дроби: {self.ipart()}")

    def normalize(self):
        g = gsd(self.__first, self.__second)
        self.__first //= g
        self.__second //= g

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    def ipart(self):
        return self.__first // self.__second
