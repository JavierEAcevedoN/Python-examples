"""Escribir un programa que reciba una cadena de caracteres e imprima el tamaño de la cadena, la cadena en mayusculas, la cadena en minusculas, la cadena invertida y la segunda mitad de la cadena."""
def primos(num):
    for i in range(2, num):
        if num%i == 0:
            print("no es un numero primo")
            break
        else:
            print("es un numero primo")
            break

num = int(input("ingresa un numero "))
primos(num)