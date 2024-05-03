productos = {
    "Menta":300,
    "Chocorramo":1000,
    "Esfero":2700,
    "Chocolatina":2500,
}

print("estos son los productos disponibles")

for i,j in productos.items():
    print("producto", i, "precio", j)

producto = input("ingresa el producto ").title()
cantidad = int(input("ingresa la cantidad "))

for i in productos:
    if producto == i:
        resultado = productos[i] * cantidad
        print(f"el precio de {cantidad} {i}s es de {resultado}",)
        break
else:
    print("ese producto no esta disponible")