nombre = "Javier Eduardo Acevedo Noguera"

# tipo de variable
print(type(nombre))

# imprime mi nombre
print(nombre)

# imprimir con comillas simple y dobles
print('imprimiendo comillas "dobles" dentro de comillas simples')
print("imprimiendo comillas 'simples' dentro de comillas dobles")
print("imprimiendo comillas \"dobles\" dentro de comillas dobles")
print('imprimiendo comillas \'simples\' dentro de comillas simples')

# metiendo varibles de str en un cadena str
print(f"mi nombre es {nombre}")
# otro modo de hacerlo es
print("mi nombre es " + nombre)

# concatenacion de cadenas de texto
a = "Hola"
b = "Mundo"
print(a + " " + b)

# longitud de una cadena en este caso mi nombre contando espacios
print(len(nombre))

# imprimir una letra de la cadena de texto
print(nombre[1])

# imprimir una parte de la cadena de texto
print(nombre[0:6])

# imprimir mi nombre alreves
print(nombre[::-1])

# buscar un texto dentro de la cadena
print(nombre.find("Eduardo"))

# remplazar el texto de una cadena (buscando el texto)
print(nombre.replace("Acevedo", "_________"))
# remplazar el texto de una cadena (buscando por los caracteres)
print(nombre.replace(nombre[7:14], "_________"))

# imprimir mi nombre en minusculas
print(nombre.lower())
# imprimir mi nombre en mayusculas
print(nombre.upper())
# imprimir mi nombre con la primera letra en mayuscula
print(nombre.capitalize())
# imprimir mi nombre con la primera letra de cada texto en mayuscula
print(nombre.title())

# separar los espacios de mi nombre
nombre_separado = nombre.split(" ")
print(nombre_separado)

# unir los espacios de mi nombre con -
print("-".join(nombre_separado))