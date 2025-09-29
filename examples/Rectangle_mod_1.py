class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, w):
        self.__width = w

    def get_height(self):
        return self.__height

    def set_height(self, h):
        self.__height = h

    def area(self):
        return self.__width * self.__height


def main():
    rect = Rectangle(10, 5)
    print(f"Width: {rect.get_width()}")
    print(f"Height: {rect.get_height()}")
    print(f"Width: {rect._Rectangle__width}")
    print(f"Height: {rect._Rectangle__height}")
    print(f"Area: {rect.area()}")


if __name__ == "__main__":
    main()
