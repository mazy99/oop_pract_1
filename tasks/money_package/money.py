#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from __future__ import annotations


class Money:
    def __init__(self, rub: int, kop: int) -> None:
        self.__rub = int(rub)
        self.__kop = int(kop)

    @property
    def rub(self) -> int:
        return self.__rub

    @property
    def kop(self) -> int:
        return self.__kop

    def read(self) -> None:
        self.__rub = int(input("Введите количество рублей: "))
        self.__kop = int(input("Введите количество копеек: "))

    def display(self) -> str:
        print(f"Количество денег: {self.__rub},{self.__kop} руб.")

    def _to_kop(self) -> int:
        return self.rub * 100 + self.kop

    def normalize(self) -> None:
        if self.__kop >= 100:
            self.__rub = self.__rub + self.__kop // 100
            self.__kop = self.__kop % 100
        elif self.__kop < 0:
            self.__rub = self.__rub - (-self.__kop // 100)
            self.__kop = -self.__kop % 100

    def add(self, other: Money) -> Money:
        total = self._to_kop() + other._to_kop()
        return Money(0, total)

    def sub(self, other: Money) -> Money:
        total = self._to_kop() - other._to_kop()
        return Money(0, total)

    def div(self, other: Money) -> float:
        if other._to_kop() == 0:
            raise ZeroDivisionError
        total = round(self._to_kop() / other._to_kop())
        return total

    def div_num(self, num: float) -> Money:
        if num == 0:
            raise ZeroDivisionError
        total = self._to_kop() / num
        return Money(0, total)

    def mul_num(self, num: float) -> Money:
        total = self._to_kop() * num
        return Money(0, total)

    def eq(self, other) -> bool:
        return self._to_kop() == other._to_kop()

    def lt(self, other) -> bool:
        return self._to_kop() < other._to_kop()

    def gt(self, other) -> bool:
        return self._to_kop() > other._to_kop()

    def le(self, other) -> bool:
        return self._to_kop() <= other._to_kop()

    def ge(self, other) -> bool:
        return self._to_kop() >= other._to_kop()

    def ne(self, other) -> bool:
        return self._to_kop() != other._to_kop()
