from modules.datos import *
from modules.pedidos import *
from modules.consultas import *

pedidos = leer_json("data/pedidos.json")
catalogo = leer_csv("data/catalogo.csv")

# menu general
while True:
    choice = -1
    pagos = []
    try:
        choice = int(input("""
menu general
ingresa una de las siguientes opciones
(1) Menu de pedidos.
(2) Menu de consultas.
(0) Terminar. """))
    except Exception:
        print("ese valor no es valido")
    if choice == 1:
        catalogo,pedidos,pagos = pedido(catalogo,pedidos)
    elif choice == 2:
        pedidos = consultas(pedidos)
    elif choice == 0:
        print("terminando proceso")
        break
    guardar_json("data/pedidos.json",pedidos)
    guardar_csv("data/pagos.csv",pagos)