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