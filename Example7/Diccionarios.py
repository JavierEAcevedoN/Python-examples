# los diccionarios son una estructura de datos que permite almacenar su contenido en forma de llaver y valor

# asi se crea un diccionario

diccionario = {"color": "blanco"}

print(diccionario["color"], type(diccionario))

# tambien puede usarse dict

diccionario = dict({"color": "negro"})

print(diccionario["color"], type(diccionario))

# tambien se pueden modificar los elementos en los diccionarios

diccionario["color"] = "azul"

print(diccionario["color"])

# los diccionarios pueden tener listas, diccionarios y otros elementos adentro

persona = {
    "nombre" : "Nikolas",
    "edad" : 39,
    "ID" : "42567425744",
    "pasatiempos" : ["hacer experimentos", "estudiar"],
    "amigo" : {"nombre" : "kelvin", "edad" : 25,"ID" : "1746252852428","pasatiempos" : ["hacer experimentos", "estudiar"],}
}

print(persona["nombre"])
print(persona["edad"])
print(persona["ID"])
print(persona["pasatiempos"][1])
print(persona["amigo"]["nombre"])

# se puede usar for en los diccionarios
for i in persona:
    print(i)

for i in persona:
    print(persona[i])

for i , j in persona.items():
    print(i, ":", j)

# get tambien se puede usar para buscar elementos en el diccionario, pero ademas si no encuentra el elemento le puedes poner que haga algo adicional

print(persona.get("a", "no encontrado"))

# con clear su pueden eliminar todos los elementos del diccionario

persona.clear()
print(persona)

# con keys su pueden obtener los indices de todos los elementos del diccionario
diccionario["color1"] = "amarillo"
print(diccionario.keys())

# con values su pueden obtener los valores de cada indice los elementos del diccionario

print(diccionario.values())

# con pop su pueden los elementos especificados del diccionario

print(diccionario.pop("color1"))

#y si no lo encuntra devulelve un default

print(diccionario.pop("color1", "no encontrado"))