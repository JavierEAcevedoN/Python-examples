# los operadores de conversion nos permiten transformar un tipo de dato a otro 

# para pasar un dato a entero
ejemplo = "1"
print(ejemplo, type(ejemplo))
ejemplo = int(ejemplo)
print(ejemplo, type(ejemplo))

# para pasar un dato a decimal
ejemplo = "24"
print(ejemplo, type(ejemplo))
ejemplo = float(ejemplo)
print(ejemplo, type(ejemplo))

# para pasar un dato a cadena de texto
ejemplo = 100
print(ejemplo, type(ejemplo))
ejemplo = str(ejemplo)
print(ejemplo, type(ejemplo))

# para pasar un dato a un arreglo
ejemplo = "hola"
print(ejemplo, type(ejemplo))
ejemplo = list(ejemplo)
print(ejemplo, type(ejemplo))

# para pasar de un decimal a un binario
ejemplo = 50
print(ejemplo, type(ejemplo))
ejemplo = bin(ejemplo)
print(ejemplo, type(ejemplo))

# para pasar de un decimal a un octal
ejemplo = 50
print(ejemplo, type(ejemplo))
ejemplo = oct(ejemplo)
print(ejemplo, type(ejemplo))

# para pasar de un decimal a un hexagecimal
ejemplo = 50
print(ejemplo, type(ejemplo))
ejemplo = hex(ejemplo)
print(ejemplo, type(ejemplo))