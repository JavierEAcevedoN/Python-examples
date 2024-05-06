# tambien se pueden importar modulos de python
from collections.abc import Iterable

num = 0
caracter = "abc"
lista=["l","i","s","t","a"]
tupla = ("t","u","p","l","a")
diccionario = {"diccionario":"si"}

def es_iterable(obj):
    print(issubclass(type(obj), Iterable))

es_iterable(num)
es_iterable(caracter)
es_iterable(lista)
es_iterable(tupla)
es_iterable(diccionario)

# otro modo de iterar es con la funcion iter y next

repisa = ["Peluche","Libro","Celular","Lampara"]
objetos =iter(repisa)

print(next(objetos))
print(next(objetos))
print(next(objetos))
print(next(objetos))

repisa = "Javier"
objetos =iter(repisa)

print(next(objetos))
print(next(objetos))
print(next(objetos))
print(next(objetos))
print(next(objetos))
print(next(objetos))