""" Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la 
contraseña correcta. """
password = "Campus2023"
while True:
    input_password = input("ingresa la contraseña ")
    if input_password == password:
        print("contraseña correcta")
        break
    else:
        print("contraseña incorrecta")