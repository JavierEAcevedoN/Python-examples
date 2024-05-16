from datos import *
from crud import *
tarjetas = leerJson("tarjetas.json")

while True:
    choice = -1
    try:
        choice = int(input("""
ingresa la opcion: 
(1) Añadir tarjeta.
(2) Modificar tarjeta.
(3) Eliminar tarjeta.
(4) Listar tarjetas.
(0) Terminar. """))
    except Exception:
        print("ese valor no es valido")

    if choice == 1:
        tarjetas = añadir_tarjeta(tarjetas)
    elif choice == 2:
        tarjetas = modificar_tarjeta(tarjetas)
    elif choice == 3:
        tarjetas = eliminar_tarjeta(tarjetas)
    elif choice == 4:
        tarjetas = listar_tarjetas(tarjetas)
    elif choice == 0:
        print("terminando proceso")
        break
    guardarJson(tarjetas,"tarjetas.json")