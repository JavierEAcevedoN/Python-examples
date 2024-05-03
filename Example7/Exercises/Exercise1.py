""" Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario. """
divisas = {
    "Euro":"€",
    "Dollar":"$",
    "Yen":"¥"
}

decision = input("ingresa la divisa de las disponibles (euro, dollar o yen) ").title()
for i in divisas:
    if decision == i:
        print(f"el simbolo de la divisa ingresada es {divisas[i]}")
        break
else:
    print("esa divisa no esta disponible")