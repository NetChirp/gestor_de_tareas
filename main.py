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

    print(f"{BLUE_COLOR}--- TAREAS ACTUALES ---{RESET_COLOR}")
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


def change_task_name(index_to_change: int, new_name: str):
    # Ajustar el índice de 1-basado a 0-basado
    list_index = index_to_change - 1

    # Validación básica del índice
    if 0 <= list_index < len(tasks):
        old_name = tasks[list_index][0]

        # Comprobar si el nuevo nombre ya existe (opcional, pero buena práctica para evitar duplicados)
        # Se puede usar una versión modificada de search_task o simplemente iterar
        name_exists = any(
            task[0].lower() == new_name.lower()
            for i, task in enumerate(tasks)
            if i != list_index
        )

        if name_exists:
            print(
                f"\n{YELLOW_COLOR}El nombre de tarea '{new_name}' ya existe. Por favor, elige otro.{RESET_COLOR}\n"
            )
            return tasks

        # Actualizar el nombre (índice 0 dentro de la lista de la tarea)
        tasks[list_index][0] = new_name
        print(
            f"\n{BLUE_COLOR}El nombre de la tarea '{old_name}' ha cambiado a '{new_name}'.{RESET_COLOR}\n"
        )
    else:
        print(
            f"\n{RED_COLOR}Error: Índice de tarea no válido ({index_to_change}).{RESET_COLOR}\n"
        )

    return tasks


while execute:
    print("----------------------")
    print(f"{BLUE_COLOR}OPCIONES{RESET_COLOR}")
    print(f"{BLUE_COLOR}[1]{RESET_COLOR} Añadir una nueva tarea")
    print(f"{BLUE_COLOR}[2]{RESET_COLOR} Consultar tareas")
    print(f"{BLUE_COLOR}[3]{RESET_COLOR} Gestionar tareas")
    print(f"{BLUE_COLOR}[4]{RESET_COLOR} Salir del programa")
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
                display_tasks()
            case 3:
                os.system("clear")
                display_tasks()
                index_of_task: int = int(
                    input(
                        f"{YELLOW_COLOR}Introduced el indice de la tarea a gestionar: {RESET_COLOR}"
                    )
                )

                print(f"{BLUE_COLOR}--- ACCIONES ---{RESET_COLOR}")
                print(f"{BLUE_COLOR}[1]{RESET_COLOR} Cambiar nombre")
                print(f"{BLUE_COLOR}[2]{RESET_COLOR} Cambiar estado")
                print(f"{BLUE_COLOR} --- FIN --- {RESET_COLOR}")
                try:
                    to_do = int(input("Opcion a realizar (numero): "))
                    match to_do:
                        case 1:
                            new_task_name: str = input("Introduce el nuevo nombre")

                            pass
                        case 2:
                            pass
                except ValueError:
                    print(
                        f"{RED_COLOR} Debes introducir 1 u 2 como acción!{RESET_COLOR}"
                    )
            case 4:
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
