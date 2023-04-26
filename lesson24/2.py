from abc import abstractmethod
from math import pi
from typing import Union


class Shape:
    def print_shape_info(self):
        print(f"{self.__class__.__name__}: area ({self.area()}); perimeter({self.perimeter()})")

    @abstractmethod
    def area(self, *args, **kwargs):
        ...

    @abstractmethod
    def perimeter(self, *args, **kwargs):
        ...


class Rectangle(Shape):
    def __init__(self, a: Union[int, float], b: Union[int, float]):
        self.a = a
        self.b = b

    def area(self) -> Union[int, float]:
        return self.a * self.b

    def perimeter(self) -> Union[int, float]:
        return 2 * (self.a + self.b)


class Circle(Shape):
    def __init__(self, r: Union[int, float]):
        self.r = r

    def area(self) -> Union[int, float]:
        return pi * self.r ** 2

    def perimeter(self) -> Union[int, float]:
        return 2 * pi * self.r


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


r = Rectangle(2, 3)
r.print_shape_info()
s = Shape()
c = Circle(4)
c.print_shape_info()
s = Square(4)
s.print_shape_info()