# los conjuntos pueden almacenar datos como las listas pero los elementos no se pueden repetir, los elementos estan desordenados y los elementos tiene que ser inmutables

# asi se crea un conjunto

conjunto = {3,5,7,2,1}
print(conjunto, type(conjunto))

# tambien se crea asi

conjunto = set([3,5,7,2,1])
print(conjunto, type(conjunto))

# aqui se peude ver los nueros sin repetir

conjunto = {3,3,3,5,2,5,2,2,2,2,4,5,3,4,6,4,3,6,4,6,4,5,6,4,6,5}
print(conjunto, type(conjunto))

# tambien se pueden unir conjuntos

conjunto1 = {1,2,3}
conjunto2 = {4,5,6}

print(conjunto1, conjunto2)

conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)

# tambien se pueden añadir elementos al conjunto

conjunto3.add(7)
print(conjunto3)

# tambien se pueden eliminar elementos aleatoriamente en el conjunto

conjunto3.pop()
print(conjunto3)

# tambien se pueden eliminar elementos del conjunto pasandole un parametro, pero si no lo encuentra bota un error

conjunto3.remove(2)
print(conjunto3)

# tambien se pueden eliminar elementos del conjunto pasandole un parametro, pero si no lo encuentra no pasa nada

conjunto3.discard(1)
print(conjunto3)

# tambien se pueden eliminar todos  los elementos del conjunto

conjunto3.clear()
print(conjunto3)