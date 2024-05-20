# menu pedidos
def pedido(catalogo,pedidos):
    while True:
        choice = -1
        try:
            choice = int(input("""
menu de pedidos
ingresa una de las siguientes opciones
(1) Hacer un pedido.
(2) Modificar un pedido.
(3) Eliminar un pedido.
(0) Terminar. """))
        except Exception:
            print("ese valor no es valido")
        if choice == 1:
            pedidos = registrar_pedido(catalogo,pedidos)
        elif choice == 2:
            pedidos = modificar_pedido(catalogo,pedidos)
        elif choice == 3:
            pedidos = eliminar_pedido(pedidos)
        elif choice == 0:
            print("terminando proceso")
            return catalogo,pedidos

# registar pedido
def registrar_pedido(catalogo,pedidos):
    catalogo = list(catalogo)
    pedidos = dict(pedidos)
    cc_cliente = 0
    categoria = 0
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
            print("ya hiciste un pedido")
            return pedidos
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
    pedidos[categoria].append(
        {
            "cc_cliente":cc_cliente,
            "pedido":pedido,
            "pago":False
        }
    )
    return pedidos

# modificar pedido
def modificar_pedido(catalogo,pedidos):
    pedidos = dict(pedidos)
    cc_cliente = 0
    categoria = 0
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
            i["pedido"] = pedido
            return pedidos
    print("no se encontro a ese usuario")
    return pedidos

# eliminar pedido
def eliminar_pedido(pedidos):
    pedidos = dict(pedidos)
    cc_cliente = 0
    categoria = 0
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
            pedidos[categoria].remove(i)
            return pedidos
    print("no se encontro a ese usuario")
    return pedidos