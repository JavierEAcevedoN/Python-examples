"""Escribir una función que reciba un número entero positivo y devuelva su factorial."""
def factorial(num):
    factor = 1
    for i in range(1, num+1):
        factor *= i
    print("el factorial del numero " + str(num) + " es " + str(factor))

num = int(input("ingresa un numero "))
factorial(num)