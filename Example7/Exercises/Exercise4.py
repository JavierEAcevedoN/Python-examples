""" Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario. """
informacion = {}

informacion["nombre"] = input("ingresa tu nombre ")
print(f"se a ingresado el nombre {informacion['nombre']}")

informacion["edad"] = input("ingresa tu edad ")
print(f"se a ingresado la edad {informacion['edad']}")

informacion["sexo"] = input("ingresa tu sexo ")
print(f"se a ingresado el sexo {informacion['sexo']}")

informacion["telefono"] = input("ingresa tu telefono ")
print(f"se a ingresado el telefono {informacion['telefono']}")

informacion["correo electronico"] = input("ingresa tu correo electronico ")
print(f"se a ingresado el correo electronico {informacion['correo electronico']}")