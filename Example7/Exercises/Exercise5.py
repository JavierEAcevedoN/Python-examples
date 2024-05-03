""" Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total """
cesta = {}
articulo = ""
precio = 0

while True:
    articulo = input("ingresa el articulo ")
    if articulo.lower() == "salir":
        break
    else:
        precio = int(input("ingresa el precio "))
        cesta.update({articulo : precio})

lista_c = ""
for i in cesta:
    lista_c += i + ", "
print(lista_c)

total = 0
for i in cesta.values():
    total += i

print(f"de los articulos {lista_c}el valor total es {total}")