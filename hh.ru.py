import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)


def test_circle_area():
    c = Circle(1)
    assert math.isclose(c.area(), math.pi)


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)


def test_triangle_is_right():
    t = Triangle(3, 4, 5)
    assert t.is_right() == True
    t2 = Triangle(3, 3, 3)
    assert t2.is_right() == False


if __name__ == "__main__":
    test_circle_area()
    test_triangle_area()
    test_triangle_is_right()
    print("Все тесты завершены.")
