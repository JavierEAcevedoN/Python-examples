""" Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>. """
informacion = {}

informacion["nombre"] = input("ingresa tu nombre ")
informacion["edad"] = input("ingresa tu edad ")
informacion["direccion"] = input("ingresa tu direccion ")
informacion["telefono"] = input("ingresa tu telefono ")

print(f"{informacion['nombre']} tiene {informacion['edad']} años, vive en {informacion['direccion']} y su número de teléfono es {informacion['telefono']}")