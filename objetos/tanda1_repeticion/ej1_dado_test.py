from ej1_dado import *

if __name__ == '__main__':
    dado1 = Dado()
    dado2 = Dado()

    print(dado1)
    print(dado2)

    dado1.lanzar()

    print(dado1)
    print(dado2)

    print(dado1.tirada)
    print(dado2.tirada)