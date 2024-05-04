""" Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro. """

facturas = {}

def agregarfactura(factura):
    factura = dict
    numero = int(input("ingresa el numero de la factura "))
    precio = int(input("ingresa el precio de la factura "))
    factura.update({numero : precio})

def eliminarfactura(factura):
    factura = dict
    numero = int(input("ingresa el numero de la factura "))
    factura.pop(numero, "no se encontro esa factura")

choice = 4

while True:
    choice = int(input("0 para terminar, 1 para agregar una factura, 2 para pagar una factura "))
    if choice == 0:
        print("terminando el proceso")
        break
    elif choice == 1:
        agregarfactura(facturas)
    elif choice == 2:
        eliminarfactura(facturas)
    elif choice == 3:
        for i,j in facturas.items():
            print(i, "=", j)