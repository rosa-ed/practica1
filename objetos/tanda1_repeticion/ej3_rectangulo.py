# 3. Implementa la clase Rectángulo (determinado por dos objetos Point) que además de su constructor,
# tendrá dos métodos para calcular su área y su perímetro que tienes que transformar en propiedades.
# Implementa también un test que cree dos puntos y un rectángulo a partir de estos dos puntos
# y que muestre el área y perímetro de dicho rectángulo.

from __future__ import annotations
from typeguard import typechecked
from ej2_punto import Point

@typechecked
class Rectangulo:

    def __init__(self, punto1:Point, punto2:Point):
        self.__punto1 = punto1
        self.__punto2 = punto2

    @property
    def punto1(self):
        return self.__punto1

    @property
    def punto2(self):
        return self.__punto2

    @punto1.setter
    def punto1(self, value:Point):
        self.__punto1 = value

    @punto2.setter
    def punto2(self, value:Point):
        self.__punto2 = value

    @property
    def area(self):
        return abs(self.punto1.x - self.punto2.x) * abs(self.punto1.y - self.punto2.y)

    @property
    def perimetro(self):
        return abs(self.punto1.x - self.punto2.x) * 2 + abs(self.punto1.y - self.punto2.y) * 2

    def __str__(self):
        return f"El rectángulo se forma de los puntos {self.punto1} y {self.punto2} y su área es {self.area} y el perímetro {self.perimetro}"
