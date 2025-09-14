class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, w):
        if w>0:
            self.__width = w
        else:
            raise ValueError
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        if h>0:
            self.__height = h
        else:
            raise ValueError
    def area(self):
        return self.__width * self.__height

def main():
    rect = Rectangle(10, 5)
    print(f"Width: {rect.width}")
    print(f"Height: {rect.height}")
    print(f"Area: {rect.area()}")

if __name__ == "__main__":
    main()