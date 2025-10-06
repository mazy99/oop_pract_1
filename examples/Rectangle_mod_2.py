#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, w) -> None:
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, h) -> None:
        if h > 0:
            self.__height = h
        else:
            raise ValueError

    def area(self) -> int:
        return self.__width * self.__height


def main() -> None:
    rect = Rectangle(10, 5)
    print(f"Width: {rect.width}")
    print(f"Height: {rect.height}")
    print(f"Area: {rect.area()}")


if __name__ == "__main__":
    main()
