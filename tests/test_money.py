from io import StringIO
from unittest.mock import patch

import pytest

from tasks.money import Money


def test_io_read():
    money = Money(5, 20)

    with patch("builtins.input", side_effect=["5", "20"]):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            money.read()
            money.display()

            output = mock_stdout.getvalue()
            assert money.rub == 5
            assert money.kop == 20
            assert "Количество денег: 5,20 руб." in output


def test_add():
    m1 = Money(5, 20)
    m2 = Money(10, 30)

    result = m1.add(m2)
    result.normalize()

    assert result.rub == 15
    assert result.kop == 50


def test_sub():
    m1 = Money(10, 30)
    m2 = Money(5, 20)

    result = m1.sub(m2)
    result.normalize()

    assert result.rub == 5
    assert result.kop == 10

    m3 = Money(10, 30)
    m4 = Money(10, 30)

    result = m3.sub(m4)
    result.normalize()

    assert result.rub == 0
    assert result.kop == 0

    m5 = Money(5, 20)
    m6 = Money(10, 30)

    result = m5.sub(m6)
    result.normalize()

    assert result.rub == -5
    assert result.kop == 10


def test_div():
    m1 = Money(20, 60)
    m2 = Money(10, 30)

    result = m1.div(m2)

    assert result == 2

    m3 = Money(10, 30)
    m4 = Money(10, 30)

    result = m3.div(m4)

    assert result == 1

    m5 = Money(10, 20)
    m6 = Money(5, 20)

    result = m5.div(m6)

    assert result == 2

    m7 = Money(5, 20)
    m8 = Money(10, 20)

    result = m7.div(m8)

    assert result == 1

    m9 = Money(5, 20)
    m10 = Money(0, 0)

    with pytest.raises(ZeroDivisionError):
        result = m9.div(m10)


def test_div_num():
    m1 = Money(20, 60)
    m2 = 2

    result = m1.div_num(m2)
    result.normalize()

    assert result.rub == 10
    assert result.kop == 30

    m3 = Money(0, 30)
    m4 = 2

    result = m3.div_num(m4)
    result.normalize()

    assert result.rub == 0
    assert result.kop == 15

    m5 = Money(10, 20)
    m6 = 0

    with pytest.raises(ZeroDivisionError):
        result = m5.div_num(m6)


def test_mul_num():
    m1 = Money(20, 60)
    m2 = 2

    result = m1.mul_num(m2)
    result.normalize()

    assert result.rub == 41
    assert result.kop == 20

    m1 = Money(20, 60)
    m2 = 0

    result = m1.mul_num(m2)
    result.normalize()

    assert result.rub == 0
    assert result.kop == 0


def test_eq():
    m1 = Money(20, 60)
    m2 = Money(20, 60)

    assert m1.eq(m2)


def test_lt():
    m1 = Money(20, 60)
    m2 = Money(10, 30)

    assert m2.lt(m1)


def test_gt():
    m1 = Money(20, 60)
    m2 = Money(10, 30)

    assert m1.gt(m2)


def test_le():
    m1 = Money(20, 60)
    m2 = Money(10, 30)

    assert m2.le(m1)


def test_ge():
    m1 = Money(20, 60)
    m2 = Money(10, 30)

    assert m1.ge(m2)


def test_ne():
    m1 = Money(20, 60)
    m2 = Money(10, 30)

    assert m1.ne(m2)
