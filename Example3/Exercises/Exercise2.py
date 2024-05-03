"""Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""
def iva(factura, iva):
    if iva == "":
        iva = 21
    iva = int(iva)
    print("la factura aplicandole el iva es de " + str(float(factura*(iva/100))))

factura = int(input("ingresa el precio de la factura "))
porcentaje_iva = input("ingresa el precio de la factura " )

iva(factura, porcentaje_iva)