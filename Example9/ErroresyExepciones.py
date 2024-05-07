try:
    num1 = int(input("ingrese un numero "))
    num2 = int(input("ingrese un numero "))
    resultado = num1/num2
except ZeroDivisionError:
    print("no se puede dividir en cero")
except ValueError:
    print("tienes que ingresar un numero")
else:
    print(f"la division es {resultado}")