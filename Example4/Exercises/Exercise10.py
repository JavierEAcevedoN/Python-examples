"""Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media."""
length = int(input("cuantos numeros vas a ingresar "))
numeros = []
promedio = 0
for i in range(length):
    numeros.append(int(input(f"ingresa el {i+1}º numero ")))

for i in numeros:
    promedio += i

print(f"el promedio de los numeros ingresados es {promedio/length}")