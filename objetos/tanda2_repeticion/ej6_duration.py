# 6. Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo y se crean de la forma:
#
# t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.
#
# t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.
#
# t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2
#
# Crea los getters y setters mediante propiedades y métodos para:
#
# Sumar y restar objetos de la clase sobrecargando operadores (el resultado es otro objeto).
# Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
# Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.

class Duration:

    def __init__(self, horas, minutos, segundos):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    @property
    def horas(self):
        return self.__horas

    @property
    def minutos(self):
        return self.__minutos

    @property
    def segundos(self):
        return self.__segundos

    @horas.setter
    def horas(self, horas):
        self.__horas = horas

    @minutos.setter
    def minutos(self, minutos):
        self.__minutos = minutos

    @segundos.setter
    def segundos(self, segundos):
        self.__segundos = segundos

    def __add__(self, other):
        return Duration(self.horas + other.horas, self.minutos + other.minutos, self.segundos + other.segundos)

    def __sub__(self, other):
        return Duration(self.horas - other.horas, self.minutos - other.minutos, self.segundos - other.segundos)

    def __str__(self):
        return f'Duration {self.horas} horas {self.minutos} minutos {self.segundos} segundos'