from money import Money

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
