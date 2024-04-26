numero = int(input("ingresa un numero "))
impares = ""

for i in range(1, numero+1):
    if i%2 == 1:
        impares += str(i)
        impares += ", " if i < numero else ""

print(impares)