class FractionIO:
    def read(self, fraction):
        fraction.first = int(input("Введите числитель: "))
        fraction.second = int(input("Введите знаменатель: "))

        self.write(fraction)

    def write(self, fraction):
        print(f"{fraction.first}/{fraction.second}")
        print(f"Целая часть дроби: {fraction.ipart()}")


class FractionPart:
    def __init__(self,first=0,second=1):
        if second == 0:
            raise ValueError("Знаменатель не может быть 0")
        
        self.__first = int(abs(first))
        self.__second = int(abs(second))

    @property
    def first(self):
                return self.__first
    @first.setter
    def first(self, value):
        self.__first = int(abs(value))

    @property
    def second(self):
                return self.__second
    @second.setter
    def second(self, value):
        value = int(abs(value))
        if value == 0:
              raise ValueError("Знаменатель не может быть 0")
        self.__second = value
    
    def ipart(self):
        return self.__first // self.__second

           
frac = FractionPart(5,2)
io = FractionIO()
io.read(frac)