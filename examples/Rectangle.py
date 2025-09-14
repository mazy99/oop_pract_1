class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    def get_width(self):
        return self._width
    def set_width(self, w):        
        self._width = w
    def get_height(self):
        return self._height
    def set_height(self, h):
        self._height = h
    def area(self):
        return self._width * self._height

def main():
    rect = Rectangle(10, 5)
    print(f"Width: {rect.get_width()}")
    print(f"Height: {rect.get_height()}")
    print(f"Area: {rect.area()}")
if __name__ == "__main__":
    main()