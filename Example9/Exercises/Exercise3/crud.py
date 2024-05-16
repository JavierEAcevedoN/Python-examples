from datetime import datetime

# añadir cliente
def añadir_cliente(datos):
    datos = list(datos)
    # pedir la informacion
    nombre = input("ingresa el nombre del cliente ")
    try:
        cc = int(input("ingresa la cedula de ciudadania del cliente "))
        if cc < 1:
            print("no se permiten numeros negativos")
            return datos
    except Exception:
        print("ese valor no es valido")
        return datos
    # verificar si la numero ya existe
    for i in datos:
        if cc == i["cc"]:
            print("ese cc no esta disponible")
            return datos
    try:
        contacto = int(input("ingresa el numero del cliente "))
    except Exception:
        print("ese valor no es valido")
        return datos
    sexo = input("ingresa el sexo del cliente ")
    # si no existe la numero, se crea la tarjeta
    datos.append(
        {
            "nombre": nombre.capitalize(),
            "cc": cc,
            "contacto": contacto,
            "sexo": sexo.capitalize(),
            "tarjetas":[]
        }
    )
    print("tarjeta resgistrada")
    return datos

# modificar cliente
def modificar_cliente(datos):
    datos = list(datos)
    # pedir la informacion
    try:
        cc = int(input("ingresa la cedula de ciudadania del cliente "))
    except Exception:
        print("ese valor no es valido")
        return datos
    # verificar si la numero ya existe
    for i in range(len(datos)):
        if cc == datos[i]["cc"]:
            try:
                contacto = int(input("ingresa el numero del cliente "))
            except Exception:
                print("ese valor no es valido")
                return datos
            sexo = input("ingresa el sexo del cliente ")
            datos[i]["contacto"] = contacto
            datos[i]["sexo"] = sexo
            print("cliente modificado")
            return datos
    print("no se encontro al cliente")
    return datos

# eliminar cliente
def eliminar_cliente(datos):
    datos = list(datos)
    try:
        cc = int(input("ingresa la cedula de ciudadania del cliente "))
    except Exception:
        print("ese valor no es valido")
        return datos
    # verificar si la numero ya existe
    for i in range(len(datos)):
        if cc == datos[i]["cc"]:
            datos.pop(i)
            print("cliente eliminado")
            return datos
    print("no se encontro ese cliente")
    return datos

# mostrar todos los clientes
def listar_clientes(datos):
    datos = list(datos)
    for i in datos:
        print("")
        print("nombre :",i["nombre"])
        print("cc :",i["cc"])
        print("contacto :",i["contacto"])
        print("sexo :",i["sexo"])
        print("terjetas :")
        for j in i["tarjetas"]:
            print("")
            for k in j:
                print(f"\t{k} : {j[k]}")
    return datos

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
        for j in i["tarjetas"]:
            if numero == j["numero"]:
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
    # si no existe la numero, se crea la tarjeta
    try:
        cc = int(input("ingresa la cedula de ciudadania del cliente "))
        if cc < 1:
            print("no se permiten numeros negativos")
            return datos
    except Exception:
        print("ese valor no es valido")
        return datos
    for i in datos:
        if cc == i["cc"]:
            i["tarjetas"].append(
                {
                    "tipo":tipo.capitalize(),
                    "numero":numero,
                    "vcc":vcc,
                    "codigo":codigo,
                }
            )
            print("tarjeta resgistrada")
            return datos
    print("no se encontro ese cliente")
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
    for i in datos:
        for j in range(len(i["tarjetas"])):
            if numero == i["tarjetas"][j]["numero"]:
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
                # modificar los datos
                i["tarjetas"][j]["vcc"] = vcc
                i["tarjetas"][j]["codigo"] = codigo
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
        return datos
    # eliminar el tarjeta por medio del numero
    for i in datos:
        for j in range(len(i["tarjetas"])):
            if numero == i["tarjetas"][j]["numero"]:
                i["tarjetas"].pop(j)
                print("tarjeta eliminada")
                return datos
    print("no se encontro la tarjeta")
    return datos

# mostrar todas las tarjetas
def listar_tarjetas(datos):
    datos = list(datos)
    for i in datos:
        for j in i["tarjetas"]:
            print("")
            for k in j:
                print(k,":",j[k])
    return datos