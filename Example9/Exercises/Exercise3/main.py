"""  El banco "Hoy no fío, mañana tampoco" desea modernizar su plataforma de gestión de tarjetas de crédito, para esto ha analizado su operación y ha levantado los requerimientos para el nuevo sistema. Se requiere realizar un programa en Python que dé solución a los requerimientos del banco del nuevo sistema de gestión de tarjetas de crédito. Los requerimientos del sistema son los siguientes:

    El sistema debe permitir el añadir, modificar, eliminar, borrar y hacer reportes de las tarjetas de créditos emitidas.
    El sistema debe cargar la información, que está en disco, antes ingresada y guardada en el sistema. De la misma forma, cualquier operación de las tarjetas de créditos debes quedar persistentes en disco.

La información de las tarjetas de crédito es:

    El tipo de tarjeta (Master Card, Visa, Américan Express)
    El número de la tarjeta de crétido
    Mes y año de validez
    Código de verificación (número entero de tres dígitos entre 100 y 999)
    Id del cliente del banco dueño de la tarjeta

Las tarjetas de crédito son emitidas a clientes del banco. La información que se necesita registrar de los clientes es:

    Nombre del cliente
    Cedula de Ciudadanía
    Número de teléfono de contacto
    Sexo

Los informes que el sistema de gestión de tarjetas de crédito emite son los siguientes:

    Tarjetas de crédito de un cliente. Este informe emite el documento del cliente, su nombre y la información de las tarjetas de crédito registradas a su nombre.
    Información de una tarjeta de crédito. Dado el número de la tarjeta de crédito, el informe muestra toda la información de la tarjeta, incluyendo la información del cliente que la tiene asociada.
    Listado de tarjetas de crédito. Este informe lista la siguiente información de las tarjetas de crédito. El número de la tarjeta, fecha de vencimiento (mes/año), tipo de tarjeta, el número de identificación del cliente y el nombre del cliente.
    Listado de los clientes con tarjetas de crédito. Este informe lista la información de los clientes: Cédula, nombre y teléfono.
    Cantidad de tarjetas de cierto tipo. Este listado muestra la cantidad (número) de tarjetas de cierto tipo (Master, Visa o American Express) """
from datos import *
from crud import *
clientes = leerJson("clientes.json")

while True:
    choice = -1
    try:
        choice = int(input("""
ingresa la opcion: 
(1) Añadir cliente.
(2) Modificar cliente.
(3) Eliminar cliente.
(4) Listar clientes.
(5) Añadir tarjeta.
(6) Modificar tarjeta.
(7) Eliminar tarjeta.
(8) Listar tarjetas.
(0) Terminar. """))
    except Exception:
        print("ese valor no es valido")

    if choice == 1:
        clientes = añadir_cliente(clientes)
    elif choice == 2:
        clientes = modificar_cliente(clientes)
    elif choice == 3:
        clientes = eliminar_cliente(clientes)
    elif choice == 4:
        clientes = listar_clientes(clientes)
    elif choice == 5:
        clientes = añadir_tarjeta(clientes)
    elif choice == 6:
        clientes = modificar_tarjeta(clientes)
    elif choice == 7:
        clientes = eliminar_tarjeta(clientes)
    elif choice == 8:
        clientes = listar_tarjetas(clientes)
    elif choice == 0:
        print("terminando proceso")
        break
    guardarJson(clientes,"clientes.json")