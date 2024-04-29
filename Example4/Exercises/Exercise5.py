"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
recuperar = []

for i in asignaturas:
    nota = float(input(f"ingresa la nota de la materia de {i} "))
    if nota < 3.5:
        recuperar.append(i)

if any(recuperar):
    for i in range(len(recuperar)):
        print(f"la {i+1}º que tienes que recuperar es {recuperar[i]} ")
else:
    print("no tienes que recuperar ninguna materia")