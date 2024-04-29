#las listas son estructuras de datos, que son una forma organizada de almacenar, gestionar y manipular datos.

# se representan asi

lista1 = [7,"texto",True,3.5]
print(type(lista1))

# agragando un elemento a una lista ya creada

dulces1 = ["Barrilete", "Chocolatina", "Maní cubierto"]
print(dulces1)
dulces1.append("Chicle")
print(dulces1)

# sumando los elementos de una lista a otra


dulces2 = ["Nucita", "Bombonbum"]
dulces1.extend(dulces2)
print(dulces1)

# buscando un elemento en la lsita

print(dulces1[2])

# insertando elementos en cualquier posicion de la lista

dulces1.insert(2, "M&M's")
print(dulces1)

# para remplasar el elemento en cualquier posicion de la lista
dulces1[2] = "Azucar"
print(dulces1)

# para borrar elementos de una lista con el valor
dulces1.remove("Nucita")
print(dulces1)

# para borrar elementos de una lista por el indice
dulces1.pop(1)
print(dulces1)

# el elemento pop tambien devuelve el elemento eliminado
print(dulces1)
removed = dulces1.pop(1)
print(dulces1)
print(removed)

# para eliminar todos los elementos de la lista
dulces1.clear()
print(dulces1)

# para eliminar todos los elementos de la lista
dulces1.extend(dulces2)
dulces1.extend(dulces2)
dulces1.extend(dulces2)
print(dulces1)
print(dulces1.count("Nucita"))

# ordenar los elementos de una lsita en forma acendente
dulces1.sort()
print(dulces1)

# para saber si un elemneto esta en la lista
print("Nucita" in dulces1)

# para saber si una lista es otra
dulces3 = []
dulces3 = dulces1
print(dulces1 is dulces3)

# para saber si una lista esta vacia o no
dulces2.clear()
print(any(dulces2))

# copiar los valores de una lista en otra
dulces2 = dulces1.copy()
print(dulces2)

# se pueden recorrer tosods los elementos de una lista usando for

for i in dulces2:
    print(i)
# tambien se puede hacer asi
for i in range(len(dulces2)):
    print(dulces2[i])
# asi para imprimirla alreves
for i in range(len(dulces2)-1, -1, -1):
    print(dulces2[i])