""" Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a 
la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por 
pantalla el grupo que le corresponde. """
nombre = input("ingresa tu nombre ")
genero = input("ingresa tu genero ")
v_nombre = False

if genero.lower() == "mujer":
    for i in range(12):
        if nombre[0].lower() == "abcdefghijkl"[i]:
            v_nombre = True
            break
elif genero.lower() == "hombre":
    for i in range(12):
        if nombre[0].lower() == "opqrstuvwxyz"[i]:
            v_nombre = True
            break


if v_nombre:
    print("usted pertenece al grupo A")
else:
    print("usted pertenece al grupo B")