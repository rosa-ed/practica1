# 4. Implementar otra clase Dado. Por defecto el dado tendrá 6 caras.
# Tendremos tres formar de construir un dado (uno al que no se le pasa nada e inicializa el dado al azar,
# otro al que sólo se le pasa que número tiene el dado en la cara superior y otro
# con el número del dado en la cara superior y el número de caras del dado).
# Implementa los getters, el metodo roll() que tirará el dado al azar y el __str__().
# Implementa un tester que tenga un vector de 4 dados y los lance una serie de veces.

from random import randint

NUMERO_CARAS = 6

class Dado:

    def __init__(self,valor_inicial = 0, cara_dado = NUMERO_CARAS):

        self.__cara_dado = cara_dado
        if valor_inicial == 0:
            self.__valor_inicial = self.roll()
        else:
            self.__valor_inicial = valor_inicial

    def roll(self):
        return randint(1, self.__cara_dado)

    def __str__(self):
        return "El dado da"

