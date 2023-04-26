from math import pi
from typing import Union


class Square:
    def __init__(self, a):
        self.a = a

    def area(self) -> Union[int, float]:
        return self.a ** 2

    def perimeter(self) -> Union[int, float]:
        return self.a * 4


class Rectangle:
    def __init__(self, a: Union[int, float], b: Union[int, float]):
        self.a = a
        self.b = b

    def area(self) -> Union[int, float]:
        return self.a * self.b

    def perimeter(self) -> Union[int, float]:
        return 2 * (self.a + self.b)


class Circle:
    def __init__(self, r: Union[int, float]):
        self.r = r

    def area(self) -> Union[int, float]:
        return pi * self.r ** 2

    def perimeter(self) -> Union[int, float]:
        return 2 * pi * self.r


def print_shape_info(s: Union[Rectangle, Circle, Square]):
    print(f"{s.__class__.__name__}: area ({s.area()}); perimeter({s.perimeter()})")


rect1 = Rectangle(3, 4)
rect2 = Rectangle(10, 10)
square1 = Square(4)
square2 = Square(8.5)
circle1 = Circle(4)
circle2 = Circle(17.3)

# print(rect1.area(), rect1.perimeter())
# print(rect2.area(), rect2.perimeter())
# print(square1.area(), square1.perimeter())
# print(square2.area(), square2.perimeter())
# print(circle1.area(), circle1.perimeter())
# print(circle2.area(), circle2.perimeter())
#
# print(Rectangle.area(rect1), Square.area(circle1))

for shape in [rect1, rect2, square1, square2, circle1, circle2]:
    # print(shape.area(), shape.perimeter())
    print_shape_info(shape)

