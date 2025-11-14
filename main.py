# Programa monolitico para la gestión de tareas
"""

TODO: Refactor add_task function to use the strip and split methods to add the task.
TODO: Refactor search_task function to search through a parameter, sorting the zip() variable results
"""
import os

# Variables globales
execute: bool = True
tasks = []

""" 
* Estructura esperada de tasks: 

        Indice 1            Indice 2
* [['Tarea', 'estado'], ['Tarea', 'estado']]
"""

RED_COLOR = "\033[1;31;40m"
RESET_COLOR = "\033[0m"
BLUE_COLOR = "\033[1;34m"
YELLOW_COLOR = "\033[33m"


def search_task(name: str) -> bool:
    """
    Busca si una tarea con el 'name' dado ya existe en la lista 'tasks'.
    Asume que tasks es una lista de elementos (tuplas/listas), donde el nombre es el índice 0.
    """
    # TODO: Remove the unnecesary status iteration
    for task, status in tasks:
        # Solo necistamos el nombre de la tarea
        if task.lower() == name.lower():
            print(
                f"{YELLOW_COLOR}La tarea ya existe! Por favor, introduce otro nombre.{RESET_COLOR}\n"
            )
            return True  # Tarea existe

    return False  # Tarea no existe


def add_task():
    # TODO: Test this refactorization of the code. Still needs polishing
    task: str = input("Introduce la tarea: ")
    status: str = input("Introduce el estado de la tarea")
    if search_task(task):
        print("La tarea ya existe, no pueden haber duplicados.")


def remove_task(name: str):
    pass


def change_task_status(name: str, new_status: str):
    pass


while execute:
    print("----------------------")
    print(f"{BLUE_COLOR}OPCIONES{RESET_COLOR}")
    print(f"{BLUE_COLOR}[1]{RESET_COLOR} Añadir una nueva tarea")
    print(f"{BLUE_COLOR}[2]{RESET_COLOR} Consultar o gestionar tareas")
    print(f"{BLUE_COLOR}[3]{RESET_COLOR} Salir del programa")
    print("----------------------")

    try:
        selection: int = int(input("Numero de la acción a realizar: "))
        match selection:
            case 1:
                try:
                    os.system(
                        "clear"
                    )  # Targeted towards Linux / Powershell / MacOs. Won't work on cmd. Don't care
                    add_task()
                except ValueError:
                    print("Porfavor, escribe una tarea y su estado, no numeros")
            case 2:
                os.system("clear")
                pass
            case 3:
                execute = False
                break
            case _:  # Caso que se ejecutara si ninguno de los anteriores es valido
                print(f"{RED_COLOR}Caso no esperado!{RESET_COLOR}")
    except ValueError:  # Si no es un entero
        print(
            f"{RED_COLOR}El valor introducido no es valido. Introduce un numero del menu de opciones{RESET_COLOR}\n"
        )
