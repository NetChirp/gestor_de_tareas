# Programa monolitico para la gestión de tareas
"""
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

RED_COLOR = "\033[1;31m"
RESET_COLOR = "\033[0m"
BLUE_COLOR = "\033[1;34m"
YELLOW_COLOR = "\033[33m"


def display_tasks():
    if not tasks:
        print(f"{YELLOW_COLOR}No hay tareas en la lista.{RESET_COLOR}")
        return False

    print("--- TAREAS ACTUALES ---")
    # Usa enumerate para mostrar un índice visible al usuario
    for i, (task, status) in enumerate(tasks, 1):
        print(f"{BLUE_COLOR}[{i}]{RESET_COLOR} {task} - Estado: {status}")
    print("--------------------------\n")
    return True


def search_task(name: str) -> bool:
    """
    Busca si una tarea con el nombre introducido ya existe en la lista tasks'.
    Asume que tasks es una lista de elementos (tuplas/listas), donde el nombre es el índice 0.
    """
    for task, _ in tasks:
        if task.lower() == name.lower():
            print(
                f"{YELLOW_COLOR}La tarea ya existe! Por favor, introduce otro nombre.{RESET_COLOR}\n"
            )
            return True  # Tarea existe

    return False  # Tarea no existe


def add_task():
    user_task: str = input(
        f"{YELLOW_COLOR}Introduce la tarea y su estado, separado por una coma{RESET_COLOR}\nAñadir: "
    )
    user_task_formatted = [x.strip() for x in user_task.split(",")]

    if search_task(user_task):
        print("La tarea ya existe, no pueden haber duplicados.")
    else:
        tasks.append(user_task_formatted)
        os.system("clear")


def remove_task(name: str):
    removed = False

    # Utilizamos enumerate para obtener el índice y la tarea
    for index, (task_name, _) in enumerate(tasks):
        if task_name.lower() == name.lower():
            # Tarea encontrada, se elimina por índice
            del tasks[index]
            removed = True
            print(f"\n{BLUE_COLOR}Tarea '{name}' eliminada con éxito.{RESET_COLOR}\n")
            break

    if not removed:
        print(
            f"\n{RED_COLOR}Error: No se encontró la tarea '{name}' para eliminar.{RESET_COLOR}\n"
        )

    return tasks


def change_task_status(name: str, new_status: str):
    changed = False

    for index, (task_name, current_status) in enumerate(tasks):
        if task_name.lower() == name.lower():
            # Tarea encontrada, se actualiza el estado (índice 1 dentro de la lista de la tarea)
            tasks[index][1] = new_status
            changed = True
            print(
                f"\n{BLUE_COLOR}El estado de la tarea '{name}' ha cambiado a '{new_status}'.{RESET_COLOR}\n"
            )
            break  # Salir del bucle una vez actualizado

    if not changed:
        print(
            f"\n{RED_COLOR}Error: No se encontró la tarea '{name}' para cambiar su estado.{RESET_COLOR}\n"
        )

    return tasks  # Devuelve la lista modificada


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
                    os.system("clear")  #! No funcionara en el antiguo CMD de Windows
                    add_task()
                except ValueError:  # ? Does this except actually catch anything?
                    print("Porfavor, escribe una tarea y su estado, no numeros")
            case 2:
                os.system("clear")
                pass
            case 3:
                execute = False
                os.system("clear")
                break
            case _:  # Caso que se ejecutara si ninguno de los anteriores es valido
                print(f"{RED_COLOR}Caso no esperado!{RESET_COLOR}")
    except ValueError:  # Si no es un entero
        os.system("clear")
        print(
            f"{RED_COLOR}El valor introducido no es valido. Introduce un numero del menu de opciones{RESET_COLOR}\n"
        )
print(tasks)
