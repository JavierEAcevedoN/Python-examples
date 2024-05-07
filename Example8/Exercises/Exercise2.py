""" Dado el siguiente ejercicio con su solución:

Escribe un programa que genere los primeros 4 números perfectos. Un número perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos. Dicho de otra forma, un número perfecto es aquel que es amigo de sí mismo. Así, 6 es un número perfecto porque sus divisores propios positivos son 1, 2 y 3; y 6 = 1 + 2 + 3.


numeros_perfectos_encontrados = []
numero = 2

while len(numeros_perfectos_encontrados) < 4:
    suma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    if suma_divisores == numero:
        numeros_perfectos_encontrados.append(numero)

    numero += 1

print("Los primeros 4 números perfectos son:")
print(numeros_perfectos_encontrados)

Reestructura el ejercicio para que el calculo del número perfecto sea hecho con funciones y modularización. Una vez reestructurado el ejercicio, comenta línea por línea el funcionamiento del ejercicio. Recuerda que además de explicar la sentencia como código se debe explicar el propósito a nivel de la solución al problema propuesto. """


def numerosperfectos(lenght):
    # declarando variables
    numeros_perfectos_encontrados = []
    numero = 2
    # repetir hasta conseguir tantos numeros perfectos
    while len(numeros_perfectos_encontrados) < lenght:
        suma_divisores = 0
    # buscando las divisores enteros 
        for i in range(1, numero):
            if numero % i == 0:
                suma_divisores += i
    # buscando que la suma de los divisores de igual al numero
        if suma_divisores == numero:
            numeros_perfectos_encontrados.append(numero)
    # aumentar el numero que se esta buscando
        numero += 1
    # regresar la lista de numeros perfectos encontrados
    return numeros_perfectos_encontrados

numeros_perfectos_encontrados = numerosperfectos(4)
print("Los primeros 4 números perfectos son:")
print(numeros_perfectos_encontrados)