"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""
palabra = input("ingresa una palabra ")

if palabra == palabra[::-1]:
    print(f"la palabra {palabra} es un palíndromo")
else:
    print("esta palabra no es un palíndromo")