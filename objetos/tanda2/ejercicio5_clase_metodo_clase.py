"""""
5. Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

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
from __future__ import annotations
from xmlrpc.client import Boolean


class Stack:
    def __init__(self,*values,other=None):
        if other is not None and isinstance(other,Stack):
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

    def push(self,value):
        self.__values.insert(0,value)

    def pop(self):
        self.__values.pop(0)

    def top(self):
        return self.__values[0]

    def __str(self):
        return str(self.values)


pila=Stack(5,6,7)

print(pila.size)

print(pila.is_empty())

#<ila.empty()

print(pila.is_empty())

pila.push(6)

print(pila.values)

pila.pop()
print(pila.values)

pila_copia=Stack(0,other=pila)

print(pila_copia.values)