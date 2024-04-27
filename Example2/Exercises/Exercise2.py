""" Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error. """
print("ingresa dos numeros ")
num1 = int(input(""))
num2 = int(input(""))
if num2 == 0:
    print("el divisor no puede ser 0")
else:
    print("la division de los dos numeros es " + str(num1/num2))