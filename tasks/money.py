class Money:
    def __init__(self, rub: int, kop: int):
        self.__rub = int(rub)
        self.__kop = int(kop)

    @property
    def rub(self):
        return self.__rub

    @property
    def kop(self):
        return self.__kop

    def read(self):
        self.__rub = int(input("Введите количество рублей: "))
        self.__kop = int(input("Введите количество копеек: "))

    def display(self):
        print(f"Количество денег: {self.__rub},{self.__kop} руб.")

    def _to_kop(self):
        return self.rub * 100 + self.kop

    def normalize(self):
        if self.__kop >= 100:
            self.__rub = self.__rub + self.__kop // 100
            self.__kop = self.__kop % 100
        elif self.__kop < 0:
            self.__rub = self.__rub - (-self.__kop // 100)
            self.__kop = -self.__kop % 100

    def add(self, other):
        total = self._to_kop() + other._to_kop()
        return Money(0, total)

    def sub(self, other):
        total = self._to_kop() - other._to_kop()
        return Money(0, total)

    def div(self, other):
        if other._to_kop() == 0:
            raise ZeroDivisionError
        total = round(self._to_kop() / other._to_kop())
        return total

    def div_num(self, num: float):
        if num == 0:
            raise ZeroDivisionError
        total = self._to_kop() / num
        return Money(0, total)

    def mul_num(self, num: float):
        total = self._to_kop() * num
        return Money(0, total)

    def eq(self, other):
        return self._to_kop() == other._to_kop()

    def lt(self, other):
        return self._to_kop() < other._to_kop()

    def gt(self, other):
        return self._to_kop() > other._to_kop()

    def le(self, other):
        return self._to_kop() <= other._to_kop()

    def ge(self, other):
        return self._to_kop() >= other._to_kop()

    def ne(self, other):
        return self._to_kop() != other._to_kop()


if __name__ == "__main__":
    money_1 = Money(1, 2)
    money_2 = Money(3, 4)

    result_1 = money_1.add(money_2)
    result_1.normalize()
    result_1.display()

    money_3 = Money(5, 6)
    money_4 = Money(7, 8)

    result_2 = money_3.sub(money_4)
    result_2.normalize()
    result_2.display()

    money_5 = Money(10, 40)
    money_6 = Money(5, 20)

    result_3 = money_5.div(money_6)
    print(result_3)

    money_7 = Money(13, 14)
    result_4 = money_7.div_num(2)
    result_4.normalize()
    result_4.display()

    money_8 = Money(15, 16)
    result_5 = money_8.mul_num(2)
    result_5.normalize()
    result_5.display()

    print(money_1.eq(money_2))
    print(money_1.lt(money_2))
    print(money_1.gt(money_2))
    print(money_1.le(money_2))
    print(money_1.ge(money_2))
    print(money_1.ne(money_2))
