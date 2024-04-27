""" Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar. """
num = int(input("ingresa un numero "))
if num == 0:
    print("el numero es 0")
elif num%2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")