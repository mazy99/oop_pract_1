#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import gcd as gsd


class FractionPart:
    def __init__(self, first: int = 0, second: int = 1) -> None:
        if second == 0:
            raise ValueError("Знаменатель не может быть 0")

        self.__first = int(abs(first))
        self.__second = int(abs(second))

        self.normalize()

    def read(self) -> None:
        self.__first = int(input("Введите числитель: "))
        self.__second = int(input("Введите знаменатель: "))

        if self.__second == 0:
            raise ValueError("Знаменатель не может быть 0")

    def display(self) -> str:
        print(f"{self.__first}/{self.__second}")
        print(f"Целая часть дроби: {self.ipart()}")

    def normalize(self) -> None:
        g = gsd(self.__first, self.__second)
        self.__first //= g
        self.__second //= g

    @property
    def first(self) -> int:
        return self.__first

    @property
    def second(self) -> int:
        return self.__second

    def ipart(self) -> int:
        return self.__first // self.__second
