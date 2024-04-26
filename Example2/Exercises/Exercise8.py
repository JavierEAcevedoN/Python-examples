edad = int(input("ingresa tu edad "))

if edad <= 0:
    print("ingresa un edad valida")
else:
    for i in range(edad):
        print(i+1)