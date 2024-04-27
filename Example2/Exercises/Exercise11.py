""" Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la 
inversión cada año que dura la inversión. """
inversion = int(input("ingresa la cantidad a invertir "))
interes = int(input("ingresa el interes anual "))
years = int(input("ingresa la cantidad de años "))

for i in range(years):
    print(f"en el {i+1}º año las ganancias fueron " + str(inversion*(interes/100)))