# en python hay 4 tipos de datos

# uno de los tipos de dato es el booleano

# el tipo de dato booleano se asigna asi
booleano = True
print(booleano)

# y este el el tipo de variable
print(type(booleano))

# y asi para el falso
booleano = False
print(booleano)

# tambien se puede sacar haciendolo con un operador de relaciones
# 5 es menor que 3, no
booleano = 5<3
print(booleano)
# 5 es mayor que 3, no
booleano = 5>3
print(booleano)
# 5 es menor o igual que 3, no
booleano = 5<=3
print(booleano)
# 5 es mayor o igual que 3, no
booleano = 5>=3
print(booleano)
# 5 es igual a 3, no
booleano = 5==3
print(booleano)
# 5 es diferente de 3, no
booleano = 5!=3
print(booleano)

# los booleanos se pueden usar en operadores logicos
# aqui se puede ver utilizando AND
print(True and True)
# aqui se puede ver utilizando OR
print(True or False)
# aqui se puede ver utilizando NOT
print(not False)