from ejercicio2 import *

if __name__ == "__main__":

    punto = Punto(4,3)
    print(punto)
    print(punto.x)
    print(repr(punto))
    punto.x = 0
    print(punto)
    punto.invertir_coordenadas()
    print(punto)