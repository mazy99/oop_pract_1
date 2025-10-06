#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def get_width(self) -> int:
        return self._width

    def set_width(self, w) -> None:
        self._width = w

    def get_height(self) -> int:
        return self._height

    def set_height(self, h) -> None:
        self._height = h

    def area(self) -> int:
        return self._width * self._height


def main() -> None:
    rect = Rectangle(10, 5)
    print(f"Width: {rect.get_width()}")
    print(f"Height: {rect.get_height()}")
    print(f"Area: {rect.area()}")


if __name__ == "__main__":
    main()
