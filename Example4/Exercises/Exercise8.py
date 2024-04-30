"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""
abc = "abcdefghijklmnopqrstuvwxyz"
l_contadas = [] 

def buspalabra(palabra, letra):
    contador_l = 0
    for i in palabra:
        if i == letra:
            contador_l += 1
    return contador_l

palabra = input("ingresa una palabra ")

for i in abc:
    l_contadas.append(buspalabra(palabra, i.lower()))

for i in len(l_contadas):
    print(f"se encontraron {l_contadas[i]} de la letra {abc[i]} en la palabra ingresada")