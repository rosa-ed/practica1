"""""
5. Crea una clase que represente una estructura de datos tipo pila (Cola) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:

Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
Obtener el número de elementos almacenados (tamaño).
Saber si la pila o la cola está vacía.
Vaciar completamente la pila o la cola.
Para el caso de la pila:
Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina. 
Leer el elemento superior de la pila sin retirarlo (top).
Para el caso de la cola:
Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer elemento que entró.
Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

"""""
from xmlrpc.client import Boolean


class Cola:
    def __init__(self,*values,other=None):
        if other is not None and isinstance(other,Cola):
            self.__values=other.__values.copy()
        else:
            self.__values=list(values)

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self,values):
        self.__values=values

    @property
    def size(self):
        return len(self.values)

    def is_empty(self):
        return not Boolean(self.size)

    def empty(self):
        self.__values.clear()

    def enqueue(self,value):
        self.__values.insert(0,value)

    def dequeue(self):
        return self.__values.pop(len(self.__values)-1)

    def front(self):
        return self.__values[len(self.__values)-1]

    def __str__(self):
        return str(self.values)


cola = Cola(3,4,5)

cola.enqueue(9)
print(cola)

print(cola.dequeue())

print(cola.front())
print(cola)

cola.enqueue(19)
print(cola)