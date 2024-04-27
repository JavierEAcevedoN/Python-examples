""" Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que 
pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no. """
edad = int(input("ingresa tu edad "))
ingresos = 0

if edad > 16:
    ingresos = int(input("ingresa tus ingresos "))
if ingresos >= 1000:
    print("si puedes tributar")
else:
    print("no puedes tributar")