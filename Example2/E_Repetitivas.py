# son estructuras que repiten algo

# aqui se repite si la condicion es verdadera
x = 5
while x < 100:
    print("repeticion")
    x += 5
print("termino")

# aqui se repite hasta que la condicion es verdadera
# break sirve para terminar una estructura repititiva antes
x = 5
while True:
    print("repeticion")
    x += 5
    if x == 50:
        break
print("termino")

# aqui se repite una cantidad de veces
# range sirve para moverse entre una cantidad de numeros con la cantidad de pasos a la que quieres que valla
for i in range(100):
    print(i)
print("termino")

for i in range(50, 100):
    print(i)
print("termino")

for i in range(50, 100, 2):
    print(i)
print("termino")

for i in range(100, 0, -1):
    print(i)
print("termino")

# el for tambien se puede usar para arreglos
compras = ["harina", "huevos", "azucar", "arroz"]
for i in compras:
    print(i)