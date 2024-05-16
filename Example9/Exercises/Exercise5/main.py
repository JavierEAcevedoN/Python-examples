""" La gobernación de Santander están organizando un evento deportivo en el cual se estarán organizando tres carreras:

    atletismo
    ciclismo
    patinaje

Para esta organización la gobernación comenzó a recolectar la información de los participantes en planillas manualmente, sin esperar que habría demasiada gente interesada y la cantidad de personas inscritas fue poco manejable. La gobernación requiere un programa simple hecho en Python que le permita recolectar la información de los participantes con los siguientes requerimientos.

La aplicación debe:

    Permitir registrar a los participantes mayores a 18 años y residentes en el departamento de Santander, pidiéndole seleccionar una de las tres carreras en la cual participar.
    Marcar en un ranking las 5 primeras posiciones a los participantes de cada carrera.
    No se permite la modificación de la información a los participantes.
    Mantener la información de los participantes registrados aún así la aplicación se finalice (La única forma de finalizar debe ser voluntaria del usuario que la utilice).
    Puede tener menús (haciendo la validación de la opción con números y por tanto, validando posibles excepciones)y submenús tantos como se requiera siempre y cuando sea ordenado y entendible. Para finalizar la aplicación se debe pedir confirmación
    Tener una estructura organizada   a nivel de código con módulos y funciones. """

from datos import *
from modulo import *

participantes = cargar_datos("participantes.json")

while True:
    choice = -1
    try:
        choice = int(input("""
ingresa la opcion: 
(1) Registrar participantes.
(2) Listar participantes.
(3) Mostrar ranking de cada evento.
(0) Terminar. """))
    
    except ValueError:
        print("ese valor no es valido")

    if choice == 1:
        participantes = registrar_participante(participantes)
    elif choice == 2:
        participantes = listar_participantes(participantes)
    elif choice == 3:
        participantes = mostrar_ranking(participantes)
    elif choice == 0:
        print("terminando proceso")
        break
    guardar_datos(participantes,"participantes.json")
