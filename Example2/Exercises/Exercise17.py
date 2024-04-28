""" Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará. """
palabra = ""
eco = ""

while True:
    palabra = input("ingresa cualquier palabra ")
    eco += palabra 
    eco += ", " if palabra.lower() != "salir" else ""
    if palabra.lower() == "salir":
        break

print(eco)