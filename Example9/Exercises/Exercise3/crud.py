from datetime import datetime

# añadir tarjeta
def añadir_tarjeta(datos):
    # pedir la informacion
    datos = list(datos)
    tipo = input("ingresa el tipo de tarjeta ")
    try:
        numero = int(input("ingresa el numero de la tarjeta "))
        if numero < 1:
            print("no se permiten numeros negativos")
            return datos
    except Exception:
        print("ese valor no es valido")
        return datos
    # verificar si la numero ya existe
    for i in datos:
        if numero == i["numero"]:
            print("ese numero no esta disponible")
            return datos
    vcc = input("ingresa el vcc del tarjeta ")
    try:
        codigo = int(input("ingresa el codigo de la tarjeta "))
        if not(100 <= codigo <= 999):
            print("el codigo debe estar entre 100 y 999")
            return datos
    except Exception:
        print("ese valor no es valido")
        return datos
    id_cliente = input("ingresa el id del cliente ")
    # si no existe la numero, se crea la tarjeta
    datos.append(
        {
            "tipo":tipo,
            "numero":numero,
            "vcc":vcc,
            "codigo":codigo,
            "id_clinte":id_cliente
        }
    )
    print("tarjeta resgistrada")
    return datos

# modificar la informacion del tarjeta (vcc, codigo, categoria)
def modificar_tarjeta(datos):
    datos = list(datos)
    # buscar el tarjeta por medio de la numero
    try:
        numero = int(input("ingresa el numero de la tarjeta "))
        if numero < 1:
            print("no se permiten numeros negativos")
            return datos
    except Exception:
        print("ese valor no es valido")
        return datos
    for i in range(len(datos)):
        if numero == datos[i]["numero"]:
            # pedir los datos
            vcc = input("ingresa el vcc del tarjeta ")
            try:
                codigo = int(input("ingresa el codigo de la tarjeta "))
                if not(100 <= codigo <= 999):
                    print("el codigo debe estar entre 100 y 999")
                    return datos
            except Exception:
                print("ese valor no es valido")
                return datos
            id_cliente = input("ingresa el id del cliente ")
            # modificar los datos
            datos[i]["vcc"] = vcc
            datos[i]["codigo"] = codigo
            datos[i]["id_clinte"] = id_cliente
            print("informacion de la tarjeta actualizada")
            return datos
    print("no se encontro la tarjeta")
    return datos

# eliminar tarjeta
def eliminar_tarjeta(datos):
    datos = list(datos)
    try:
        numero = int(input("ingresa el numero de la tarjeta "))
    except Exception:
        print("ese valor no es valido")
    # eliminar el tarjeta por medio de la numero
    for i in range(len(datos)):
        if numero == datos[i]["numero"]:
            datos.pop(i)
            print("tarjeta eliminada")
            return datos
    print("no se encontro la tarjeta")
    return datos

# mostrar todas las tarjetas
def listar_tarjetas(datos):
    datos = list(datos)
    for i in datos:
        print("")
        for j in i:
            print(j,":",i[j])
    return datos