# 1. Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6
# que tienen la misma probabilidad de salir y un programa de prueba.

from random import randint

class Dado:

    def __init__(self):
        self.__tirada = None

    def lanzar(self):
        self.__tirada = randint(1, 6)

    @property
    def tirada(self):
        if self.__tirada is None:
            return "No se ha lanzado el dado."
        return self.__tirada

    @tirada.setter
    def tirada(self, tirada):
        self.__tirada = tirada

    def __str__(self):
        return f'Tirada: {self.__tirada}'