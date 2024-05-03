""" Escribir un programa que guarde en un diccionario los precios de las verduras de la tabla, pregunte al usuario por una verdura, un número de kilos y muestre por pantalla el precio a pagar. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. """

productos = {
    "Brócoli":2500,
    "Pimentón":1250,
    "Arveja":3500
}

print("estos son los productos disponibles")

for i,j in productos.items():
    print("producto", i, "precio", j, "COP por kilo")

producto = input("ingresa el producto ").title()
cantidad = int(input("ingresa cuantos kilos vas a comprar "))

for i in productos:
    if producto == i:
        resultado = productos[i] * cantidad
        print(f"el precio de {cantidad} {i}s es de {resultado}",)
        break
else:
    print("ese producto no esta disponible")