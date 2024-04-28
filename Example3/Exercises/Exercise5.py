"""Escribir un programa que reciba una cadena de caracteres e imprima el tamaño de la cadena, la cadena en mayusculas, la cadena en minusculas, la cadena invertida y la segunda mitad de la cadena."""
def inf_cadena(cadena):
    print("este es el largo del texto que ingresaste (contando espacios) " + str(len(cadena)))
    print("este es el texto que ingresaste pero en mayusculas " + cadena.upper())
    print("este es el texto que ingresaste pero en minusculas " + cadena.lower())
    print("este es el texto que ingresaste pero al reves " + cadena[::-1])
    print("este es la segunda mitad del texto que ingresaste " + cadena[(int(len(cadena)/2)):(len(cadena))])

texto = input("ingresa un texto ")
inf_cadena(texto)