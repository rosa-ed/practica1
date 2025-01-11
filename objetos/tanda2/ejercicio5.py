# 5. Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).
#
# La pila y la cola permitirán estas operaciones:
#
#     Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
#     Obtener el número de elementos almacenados (tamaño).
#     Saber si la pila o la cola está vacía.
#     Vaciar completamente la pila o la cola.
#     Para el caso de la pila:
#         Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
#         Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
#         Leer el elemento superior de la pila sin retirarlo (top).
#     Para el caso de la cola:
#         Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
#         Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer elemento que entró.
#         Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

class Pila_cola():

    def __init__(self, pila,cola):
        self.__pila = pila
        self.__cola = cola

    @property
    def pila(self):
        return self.__pila
    @property
    def cola(self):
        return self.__cola

    @pila.setter
    def pila(self, pila):
        self.__pila = pila

    @cola.setter
    def cola(self, cola):
        self.__cola = cola

    def __str__(self):
        return f"Pila: {self.__pila}, Cola: {self.__cola}"


    