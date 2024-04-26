nombre = input("ingresa tu nombre ")
genero = input("ingresa tu genero ")
if genero.lower() == "mujer":
    if nombre[0].lower() == ["a","b","c","d","e","f","g","h","i","j","k","l"]:
        print("usted pertenece al grupo A")
    else:
        print("usted pertenece al grupo B")
elif genero.lower() == "hombre":
    if (nombre[0].lower()) == ["o","p","q","r","s","t","u","v","w","x","y","z"]:
        print("usted pertenece al grupo A")
    else:
        print("usted pertenece al grupo B")