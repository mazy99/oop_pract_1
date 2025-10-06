#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
from fraction_part import FractionPart


def test_fraction_io_read(monkeypatch, capsys) -> None:
    frac = FractionPart(5, 2)

    inputs = iter(["3", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    frac.read()
    frac.display()

    captured = capsys.readouterr()
    assert frac.first == 3
    assert frac.second == 4
    assert "3/4" in captured.out
    assert "Целая часть дроби: 0" in captured.out


def test_fraction_part_initialization() -> None:
    with pytest.raises(ValueError):
        FractionPart(1, 0)


def test_fraction_ipart() -> None:
    fraction = FractionPart(7, 3)
    assert fraction.ipart() == 2


def test_fraction_denominator_zero() -> None:
    with pytest.raises(ValueError, match="Знаменатель не может быть 0"):
        FractionPart(1, 0)


def test_fraction_normalization() -> None:
    fraction = FractionPart(8, 4)
    assert fraction.first == 2
    assert fraction.second == 1
    assert fraction.ipart() == 2


def test_fraction_negative_values() -> None:
    fraction = FractionPart(-3, -4)
    assert fraction.first == 3
    assert fraction.second == 4
    assert fraction.ipart() == 0
