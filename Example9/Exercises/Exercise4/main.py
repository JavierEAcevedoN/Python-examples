""" Una empresa está organizando la agenda de eventos para el mes de agosto. Por lo tanto requiere un programa que:

    Permita registrar a los participantes de los eventos de agosto pidiendo: documento, nombre, edad y cargo.
    Permita registrar los eventos  pidiendo: nombre del evento, locación y día del mes
    Permita quitar del registro a los participantes .
    Permita eliminar y/o modificar eventos.

Para participar los empleados deben cancelar un aporte de 50.000 COP. Por lo tanto el programa también debe:

    Saber cuantos empleados no han cancelado aún el aporte y cuanto dinero suma la deuda.
    Saber cuales empleados (listarlos) no han cancelado.
    No permitir quitar del registro a participantes que ya hayan pagado, pues no se aceptan devoluciones
    Marcar eventos ya realizados.
    No permitir eliminar o modificar eventos ya realizados.

Aspectos a tener en cuenta: 

    La estructura a utilizar es libre, solo se pide que sea ordenada y coherente. 
    Todo debe ser dentro de un menú que se repite para no perder la información y al presionar la opción de salida se debe pedir confirmación de la misma. 
    Se deben manejar la excepciones """

from datos import *
from participantes import *
from eventos import *

empleados = cargar_datos("eventos.json")


while True:
    choice = 11
    try:
        choice = int(input("""
ingresa la opcion: 
(1) Registrar participante.
(2) Eliminar participante.
(3) Pagar entrada participante.
(4) Registrar evento.
(5) Modificar evento.
(6) Finalizar evento.
(7) Cuales participantes que no han pagado.
(8) Cuantos participantes que no han pagado.
(9) Eventos del mes.
(10) Conocer participatentes del mes.
(0) Terminar. """))
    
    except ValueError:
        print("ese valor no es valido")

    if choice == 1:
        empleados = registrar_participante(empleados)
    elif choice == 2:
        empleados = eliminar_participante(empleados)
    elif choice == 3:
        empleados = pagar_participante(empleados)
    elif choice == 4:
        empleados = registrar_evento(empleados)
    elif choice == 5:
        empleados = modificar_evento(empleados)
    elif choice == 6:
        empleados = finalizar_evento(empleados)
    elif choice == 7:
        empleados = cuales_participantes_nopago(empleados)
    elif choice == 8:
        empleados = cuantos_participantes_nopago(empleados)
    elif choice == 9:
        empleados = eventos_mes(empleados)
    elif choice == 10:
        empleados = participantes_mes(empleados)
    elif choice == 0:
        print("terminando proceso")
        break
    
guardar_datos(empleados,"eventos.json")