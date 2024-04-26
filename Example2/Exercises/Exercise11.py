inversion = int(input("ingresa la cantidad a invertir "))
interes = int(input("ingresa el interes anual "))
years = int(input("ingresa la cantidad de años "))

for i in range(years):
    print(f"en el {i+1}º año las ganancias fueron " + str(inversion*(interes/100)))