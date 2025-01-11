# 3. Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor,
# tendrá dos métodos para calcular su área y su perímetro que tienes que transformar en propiedades.
# Implementa también un test que cree dos puntos y un rectángulo a partir de estos dos puntos
# y que muestre el área y perímetro de dicho rectángulo.

from ejercicio2 import *

class Rectangulo:

    def __init__(self, punto1:Punto, punto2:Punto):
        self.__punto1 = punto1
        self.__punto2 = punto2

    @punto1.setter
    def punto1(self, punto1):
        self.__punto1 = punto1

    @punto2.setter
    def punto2(self, punto2):
        self.__punto2 = punto2

    @property
    def area(self):
        return abs(self.__punto1.x - self.__punto2.x) * abs(self.__punto1.y - self.__punto2.y)

    @property
    def perimetro(self):
        return (abs(self.__punto1.x - self.__punto2.x) + abs(self.__punto1.y - self.__punto2.y)) * 2

    def __str__(self):
        return f"El rectángulo tiene un punto {self.__punto1} y {self.__punto2}"