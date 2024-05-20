from datos import *
registro = cargar_json("registro.json")
observaciones = cargar_csv("observaciones.csv")

for i in observaciones:
    print(i)
while True:
    choice = -1
    try:
        choice = int(input("""
ingresa la opcion: 
(1) Listar observatorios por sus codigos.
(2) Listar observatorios por su nombre.
(3) Listado de observaciones de un observatorio en particular.
(4) Listado de cantidades de observaciones.
(5) Listado de todas las observaciones a nivel nacional.
(6) Listado de todas las observaciones a nivel nacional agrupadas por observatorio.
(0) Terminar. """))
    
    except ValueError:
        print("ese valor no es valido")

    if choice == 1:
        None
    elif choice == 2:
        None
    elif choice == 3:
        None
    elif choice == 4:
        None
    elif choice == 5:
        None
    elif choice == 6:
        None
    elif choice == 0:
        print("terminando proceso")
        break
    guardar_json(registro,"registro.json")
    guardar_csv(observaciones,"observaciones.csv")

for i in range(10):
    print(i)
