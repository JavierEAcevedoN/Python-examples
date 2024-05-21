# menu consultas
def consultas(pedidos):
    while True:
        choice = -1
        try:
            choice = int(input("""
menu de consultas
ingresa una de las siguientes opciones
(1) Consultar todos los pedidos.
(2) Consultar un pedido especifico.
(0) Terminar. """))
        except Exception:
            print("ese valor no es valido")
        if choice == 1:
            pedidos = consultar_todos_pedidos(pedidos)
        elif choice == 2:
            pedidos = consultar_pedido_especifico(pedidos)
        elif choice == 0:
            print("terminando proceso")
            return pedidos

# consultar todos los pedidos
def consultar_todos_pedidos(pedidos):
    pedidos = dict(pedidos)
    for i in pedidos:
        for j in pedidos[i]:
            for k in j["pedido"]:
                print("")
                for l in k:
                    print(l,":",k[l])
    return pedidos

# comsultar un pedido especifico
def consultar_pedido_especifico(pedidos):
    pedidos = dict(pedidos)
    cc_cliente = 0
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
            for j in i["pedido"]:
                print("")
                for k in j:
                    print(k,":",j[k])
    return pedidos