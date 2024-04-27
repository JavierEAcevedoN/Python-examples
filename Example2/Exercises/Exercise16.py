""" Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase. """
frase = input("ingresa una frase ")
letra = input("ingresa una letra ")
contador_l = 0

for i in frase:
    if i == letra:
        contador_l += 1

print(f"la letra {letra} se repitio {contador_l} veces")