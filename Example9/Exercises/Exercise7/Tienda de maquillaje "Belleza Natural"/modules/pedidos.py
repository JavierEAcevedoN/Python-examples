# menu pedidos
from datetime import datetime
def pedido(catalogo,pedidos):
    catalogo = list(catalogo)
    pedidos = dict(pedidos)
    pagos = []
    while True:
        choice = -1
        try:
            choice = int(input("""
menu de pedidos
ingresa una de las siguientes opciones
(1) Hacer un pedido.
(2) Modificar un pedido.
(3) Eliminar un pedido.
(4) Pagar un pedido.
(0) Terminar. """))
        except Exception:
            print("ese valor no es valido")
        if choice == 1:
            pedidos,pagos = registrar_pedido(catalogo,pedidos,pagos)
        elif choice == 2:
            pedidos,pagos = modificar_pedido(catalogo,pedidos,pagos)
        elif choice == 3:
            pedidos = eliminar_pedido(pedidos)
        elif choice == 4:
            pedidos,pagos = pagar_pedido(pedidos,pagos)
        elif choice == 0:
            print("terminando proceso")
            return catalogo,pedidos,pagos

# registar pedido
def registrar_pedido(catalogo,pedidos,pagos):
    catalogo = list(catalogo)
    pedidos = dict(pedidos)
    pagos = list(pagos)
    cc_cliente = 0
    categoria = 0
    try:
        cc_cliente = int(input("ingresa tu cedula de ciudadania "))
        categoria = int((input("ingresa la categoria del producto (1 para base, 2 para labiales, 3 para sombras, 4 para mascaras) ")))
    except Exception:
        print("ese valor no es valido")
        return pedidos,pagos
    if categoria == 1:
        categoria = "base"
    elif categoria == 2:
        categoria = "labiales"
    elif categoria == 3:
        categoria = "sombras"
    elif categoria == 4:
        categoria = "mascaras"
    else:
        print("ese valor no es valido ")
        return pedidos,pagos
    for i in pedidos[categoria]:
        if cc_cliente == i["cc_cliente"] and not(i["pago"]):
            print("todavia no has pagado el pedido anterior")
            return pedidos,pagos
    pedido = []
    while True:
        lista = []
        for i in catalogo:
            if categoria == i["categoria"]:
                lista.append(i)
        for i in range(len(lista)):
            print("")
            print(f'{i+1}:\nproducto : {lista[i]["Producto"]}.\nnombre : {lista[i]["Nombre"]}.\nprecio : {lista[i]["Precio"]}')
        choice = 0
        print("")
        try:
            choice = int(input("ingresa el producto que quieres "))
            choice -= 1 if choice > 1 else 0
            pedido.append(lista[choice])
        except Exception:
            print("ese valor no es valido")
        terminar = "no"
        terminar = input("quieres terminar con el pedido? (si o no) ").lower()
        if terminar == "si":
            break
    print("")
    print("estos son todos los productos que acabas de pedir:")
    for i in pedido:
        print("")
        for j in i:
            print(f"\t{j} : {i[j]}")
    aceptar = input("quieres guardar el pedido? (si o no) ").lower()
    if aceptar == "si":
        print("pedido terminado")
        aceptar = input("vas a pagar de una ves? (si o no) ").lower()
        if aceptar == "si":
            pedidos[categoria].append(
                {
                    "cc_cliente":cc_cliente,
                    "pedido":pedido,
                    "pago":True
                }
            )
            total = 0
            for i in pedido:
                total += int(i["Precio"])
            pagos.append(
                [str(datetime.now().replace(microsecond=0)),total,cc_cliente]
            )
            print("el total de la compra es",total)
            return pedidos,pagos
        else:
            pedidos[categoria].append(
                {
                    "cc_cliente":cc_cliente,
                    "pedido":pedido,
                    "pago":False
                }
            )
            print("pedido pendiente")
            return pedidos,pagos
    else:
        print("pedido cancelado")
        return pedidos,pagos

# modificar pedido
def modificar_pedido(catalogo,pedidos,pagos):
    catalogo = list(catalogo)
    pedidos = dict(pedidos)
    pagos = list(pagos)
    cc_cliente = 0
    categoria = 0
    pago = False
    try:
        cc_cliente = int(input("ingresa tu cedula de ciudadania "))
        categoria = int((input("ingresa la categoria del producto (1 para base, 2 para labiales, 3 para sombras, 4 para mascaras) ")))
    except Exception:
        print("ese valor no es valido")
        return pedidos,pagos
    if categoria == 1:
        categoria = "base"
    elif categoria == 2:
        categoria = "labiales"
    elif categoria == 3:
        categoria = "sombras"
    elif categoria == 4:
        categoria = "mascaras"
    else:
        print("ese valor no es valido ")
        return pedidos,pagos
    for i in pedidos[categoria]:
        if cc_cliente == i["cc_cliente"]:
            pago = i["pago"]
            if not(i["pago"]):
                pedido = []
                while True:
                    lista = []
                    for j in catalogo:
                        if categoria == j["categoria"]:
                            lista.append(j)
                    for j in range(len(lista)):
                        print("")
                        print(f'{j+1}:\nproducto : {lista[j]["Producto"]}.\nnombre : {lista[j]["Nombre"]}.\nprecio : {lista[j]["Precio"]}')
                    choice = 0
                    print("")
                    try:
                        choice = int(input("ingresa el producto que quieres "))
                        choice -= 1 if choice > 1 else 0
                        pedido.append(lista[choice])
                    except Exception:
                        print("ese valor no es valido")
                    terminar = "no"
                    terminar = input("quieres terminar con el pedido? (si o no) ").lower()
                    if terminar == "si":
                        break
                print("")
                print("estos son todos los productos que acabas de pedir:")
                for j in pedido:
                    print("")
                    for k in j:
                        print(k,":",j[k])
                aceptar = input("quieres guardar la modificacion del pedido? (si o no) ").lower()
                if aceptar == "si":
                    i["pedido"] = pedido
                    print("pedido terminado")
                    aceptar = input("vas a pagar de una ves? (si o no) ").lower()
                    if aceptar == "si":
                        i["pago"] = True
                        total = 0
                        for j in pedido:
                            total += int(j["Precio"])
                        pagos.append(
                            [str(datetime.now().replace(microsecond=0)),total,cc_cliente]
                        )
                        print("el total de la compra es",total)
                        return pedidos,pagos
                    else:
                        print("pedido pendiente")
                else:
                    print("modificacion del pedido cancelado")
                    return pedidos,pagos
    if pago:
        print("ese usuario ya pago el pedido")
        return pedidos,pagos
    print("no se encontro a ese usuario")
    return pedidos,pagos

# eliminar pedido
def eliminar_pedido(pedidos):
    pedidos = dict(pedidos)
    cc_cliente = 0
    categoria = 0
    pago = False
    try:
        cc_cliente = int(input("ingresa tu cedula de ciudadania "))
        categoria = int((input("ingresa la categoria del producto (1 para base, 2 para labiales, 3 para sombras, 4 para mascaras) ")))
    except Exception:
        print("ese valor no es valido")
        return pedidos
    if categoria == 1:
        categoria = "base"
    elif categoria == 2:
        categoria = "labiales"
    elif categoria == 3:
        categoria = "sombras"
    elif categoria == 4:
        categoria = "mascaras"
    else:
        print("ese valor no es valido ")
        return pedidos
    for i in pedidos[categoria]:
        if cc_cliente == i["cc_cliente"]:
            pago = i["pago"]
            if not(i["pago"]):
                pedidos[categoria].remove(i)
                print("pedido eliminado")
                return pedidos
    if pago:
        print("ese usuario ya pago el pedido")
        return pedidos
    print("no se encontro a ese usuario")
    return pedidos

# pagar pedido
def pagar_pedido(pedidos,pagos):
    pedidos = dict(pedidos)
    pagos = list(pagos)
    cc_cliente = 0
    categoria = 0
    pago = False
    try:
        cc_cliente = int(input("ingresa tu cedula de ciudadania "))
        categoria = int((input("ingresa la categoria del producto (1 para base, 2 para labiales, 3 para sombras, 4 para mascaras) ")))
    except Exception:
        print("ese valor no es valido")
        return pedidos,pagos
    if categoria == 1:
        categoria = "base"
    elif categoria == 2:
        categoria = "labiales"
    elif categoria == 3:
        categoria = "sombras"
    elif categoria == 4:
        categoria = "mascaras"
    else:
        print("ese valor no es valido ")
        return pedidos,pagos
    for i in pedidos[categoria]:
        if cc_cliente == i["cc_cliente"]:
            pago = i["pago"]
            if not(i["pago"]):
                print("")
                print("estos son todos los productos que hay que pagar:")
                for j in i["pedido"]:
                    print("")
                    for k in j:
                        print(k,":",j[k])
                aceptar = input("pagar? (si o no) ").lower()
                if aceptar == "si":
                    i["pago"] = True
                    total = 0
                    for j in i["pedido"]:
                        total += int(j["Precio"])
                    pagos.append(
                        [str(datetime.now().replace(microsecond=0)),total,cc_cliente]
                    )
                    print("el total de la compra es",total)
                    return pedidos,pagos
                else:
                    print("pago cancelado")
                    return pedidos,pagos
    if pago:
        print("ese usuario ya pago el pedido")
        return pedidos,pagos
    print("no se encontro a ese usuario")
    return pedidos,pagos