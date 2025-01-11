from __future__ import annotations
from typeguard import typechecked

@typechecked
class Point:

    def __init__(self, x:int, y:int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value:int):
        self.__x = value

    @y.setter
    def y(self, value:int):
        self.__y = value

    def __add__(self, other: Point):
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other: Point):
        return Point(self.__x - other.__x, self.__y - other.__y)

    def __neg__(self):
        return Point(-self.__x, -self.__y)

    def __mul__(self, other:int):
        return Point(self.__x * other, self.__y * other)

    def __rmul__(self, other:int):
        return Point(self.__x * other, self.__y * other)

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        return f"({self.__class__} {self.__x}, {self.__y})"