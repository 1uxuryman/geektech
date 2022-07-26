class Figure:
    unit = "cm"
    def __init__(self):
        self.__calculate_perimeter()
        self.calculate_area()

    def get_perimetr(self):
        return self.__perimetr

    def set_perimetr(self, perimetr):
        self.__perimetr = perimetr

    def calculate_area(self):
        pass

    def __calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, __side_length):
        self.__side_length = __side_length
        self.calculate_area()
        self.perimetr = self.__calculate_perimeter()

    def calculate_area(self):
        return self.__side_length * 2

    def __calculate_perimeter(self):
        return self.__side_length * 4

    def info(self):
        print(f'Square side length:{self.__side_length}{self.unit} Perimet:{self.__calculate_perimeter()}{self.unit}Area:{self.calculate_area()}{self.unit}')


class Rectangle(Figure):
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def calculate_area(self):
        return self.__length * self.__width

    def __calculate_perimeter(self):
        return (self.__length + self.__width) * 2

    def info(self):
        print(f'Rectangle length:{self.__length}{self.unit}  Perimetr:{self.__calculate_perimeter()}{self.unit} Area:{self.calculate_area()}{self.unit}')


square_1 = Square(1)
square_2 = Square(3)

rec_1 = Rectangle(3, 4)
rec_2 = Rectangle(5, 5)
rec_3 = Rectangle(2, 6)

all_result = [square_1, square_2, rec_1, rec_2, rec_3]
for i in all_result:
    i.info()
