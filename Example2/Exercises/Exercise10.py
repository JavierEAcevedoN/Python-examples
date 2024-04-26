numero = int(input("ingresa un numero positivo "))
c_numeros = ""

for i in range(numero, 0, -1):
    c_numeros += str(i) 
    c_numeros += ", " if 1 < i else ""

print(c_numeros)