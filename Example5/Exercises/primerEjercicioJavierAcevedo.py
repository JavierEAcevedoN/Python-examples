""" Implementar un juego interactivo donde los jugadores deben encadenar palabras basándose en la última letra de la palabra anterior. Se utiliza una lista predefinida de palabras de la cual se selecciona aleatoriamente la primera palabra para comenzar el juego. Los jugadores alternan turnos, eligiendo palabras que cumplan con la regla de encadenamiento. Se manejan casos de palabras no válidas o duplicadas. Los jugadores tienen la opción de salir cuando lo deseen. """

print("""Bienvenido jugador

las reglas del juego son las siguientes:
Los jugadores deben encadenar palabras basándose en la última letra de la palabra anterior.
Se utiliza una lista predefinida de palabras de la cual se selecciona aleatoriamente la primera palabra para comenzar el juego.
Los jugadores alternan turnos, eligiendo palabras que cumplan con la regla de encadenamiento.
Se manejan casos de palabras no válidas o duplicadas. 

Los jugadores tienen la opción de salir cuando lo deseen (escribir salir para salir).""")

palabras = ["jugar","hablar","bilar","comer"]
print(f"la primera palabra es {palabras[3]}")

while True:
    palabras.append(input("ingresa una palabra "))
    ultima = palabras[len(palabras)-1]
    antepenultima = palabras[len(palabras)-2]

    # salir del programa
    if ultima.lower() == "salir":
        break

    # valida si la palabra es mas de 1 caracter
    elif len(ultima) < 2:
        print("esa palabra no es valida")
        palabras.pop(len(palabras)-1)
        print("la palabra tiene que tener mas de 1 caracter")
        print(f"solo se puede utilizar la ultima letra de la palabra anterior {ultima}")

    # valida si la palabra ya se habia usado antes
    elif palabras.count(ultima) > 1:
        print("esa palabra no es valida")
        print(f"no se puede repetir la palabra {ultima}, porque ya se uso")
        palabras.pop(len(palabras)-1)
        print(f"solo se puede utilizar la ultima letra de la palabra anterior {ultima}")

    # valida si la primera letra de la palabra coincide con la ultima letra de la anterior
    elif antepenultima[len(antepenultima)-1].lower() == ultima[0].lower():
        print("la palabra es valida")

    # valida si la palabra cumple las condiciones
    else:
        print("esa palabra no es valida")
        palabras.pop(len(palabras)-1)
        print(f"solo se puede utilizar la ultima letra de la palabra anterior {palabras[len(palabras)-1]}")
    print("_________________________________________________________")
