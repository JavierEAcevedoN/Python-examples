"""Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función."""
def area_criculo(radio, altura):
    area = 3.1416 * (radio**2 )
    volumen_cilindro(area, altura)

def volumen_cilindro(area, altura):
    volumen = area * altura
    print("el area del circulo es " + str(area) + " y el volumen del cilindro es " + str(volumen))


radio = float(input("ingresa un radio "))
altura = float(input("ingresa una altura "))
area_criculo(radio, altura)