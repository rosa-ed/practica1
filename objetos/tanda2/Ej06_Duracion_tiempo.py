"""
6. Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de
tiempo y se crean de la forma:

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

Sumar y restar objetos de la clase sobrecargando operadores (el resultado es otro objeto).
Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
"""
from typeguard import typechecked

@typechecked
class Duration:
    def __init__(self,hours:int,minutes:int,seconds:int):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__regularizar()


    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        self.__hours = hours

    @property
    def minutes(self):
        return self.minutes

    @minutes.setter
    def minutes(self, minutes):
        self.__minutes = minutes

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        self.__seconds = seconds


    def __str__(self):
        return f"{self.__hours}h {self.__minutes}m  {self.__seconds}s"


    def __regularizar(self):
        segundos_totales = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        self.__hours = segundos_totales // 3600
        self.__minutes = (segundos_totales % 3600) // 60
        self.__seconds = (segundos_totales % 3600) % 60


    def sumar_segundos(self,segundos):
        self.__seconds += segundos
        self.__regularizar()

    def sumar_minutos(self,minutos):
        self.__minutes += minutos
        self.__regularizar()

    def sumar_horas(self, horas):
        self.__hours += horas
        self.__regularizar()







#Test

time1 = Duration(30,183,420)

print(time1)

time1.sumar_segundos(80)
print(time1)



        

