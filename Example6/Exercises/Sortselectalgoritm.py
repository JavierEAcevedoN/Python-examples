""" El algoritmo de selection sort se basa en buscar el elemento mas pequeño, esto se hace comparando el elemento con los demás elementos de la lista para ver cual es el mas pequeño, después de encontrar el elemento se intercambia de posición con el primer elemento de la lista, después de eso se busca el siguiente elemento mas pequeño sin contar el elemento que se acaba de intercambiar, cuando encuentre el siguiente elemento mas pequeño se pone en la siguiente posición del elemento intercambiado anteriormente es decir en la segunda posición de la lista, después de eso se sigue repitiendo el proceso hasta que solo quede el ultimo elemento de la lista, el ultimo elemento no se mueve ya que no se puede intercambiar con ningún otro elemento de la lista, lo que significa que ese es el elemento mas grande. """

def ordenamientoporselecion(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i, n-1):
            if lista[i] > lista[j+1]:
                lista[i], lista[j+1] = lista[j+1], lista[i]
    print(lista)

lista = [22, 57, 33, 29, 99, 88, 57, 78, 38, 52, 69, 84, 21, 78, 92, 33, 75, 11, 23, 16]
print(lista)

ordenamientoporselecion(lista)