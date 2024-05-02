# las tuplas son parecidas a las listas solo que no son irreteables, lo que significa que no cambia en la ejecucion del codigo

# asi se crean las tuplas

tupla = (1, 2, 3)
print(tupla, type(tupla))

# se pueden asignar los elementos de una lista a una tupla

lista = [3,7,2,1,1]
tupla = tuple(lista)
print(tupla, type(tupla))

# las tuplas tambien son iterables

for i in tupla:
    print(i)

# se puede usar count para ver cuantsa veces se repite el numero ingresado como parametro

print(tupla.count(1))

# se puede usar index para buscar el elemento ingresado y devolver el indice en el que se encuentra

print(tupla.index(1))