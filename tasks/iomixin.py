class IOMixin:
    def read(self):
        self.first = int(input("Введите числитель: "))
        self.second = int(input("Введите знаменатель: "))

    def write(self):
        print(f"{self.first}/{self.second}")