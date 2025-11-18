# Programa monolitico para la gestión de tareas
"""
? Declaracion importante
Declaración de uso de IA: El unico uso de la IA en este programa ha sido el saber los
full escapecodes para los colores y que me explique errores, no implementaciones o que me añade cosas

Se mezcla el inglés y el español debido a que empece esto en inglés y luego no quise hacer un Control F y reemplazar todo
una vez que funcionaba. Y como esto es para mi github tambien, el cual es en inglés, decidi simplemente mezclarlo
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


# Task will be always the index of the task. It will kill both task and status as per our structure
def remove_task():
    show_tasks: str = input("¿Sabes el índice de la tarea? S/n\nRespuesta: ")
    if show_tasks.lower() != "s":
        display_tasks()

    try:
        index = int(input("Introduce el índice de la tarea a eliminar: "))

        # Ajustamos porque el usuario ve las tareas empezando desde 1
        real_index = index - 1

        # Comprobación básica para evitar errores
        if real_index < 0 or real_index >= len(tasks):
            print(f"{RED_COLOR}El índice no existe en la lista de tareas.{RESET_COLOR}")
            return

        # Eliminamos por índice, no por valor
        tasks.pop(real_index)
        print(f"{YELLOW_COLOR}Tarea eliminada correctamente.{RESET_COLOR}\n")
        os.system("clear")

    except ValueError:
        print(f"{RED_COLOR}Debes introducir un número válido.{RESET_COLOR}")


"""
I became way too lazy to implement this in the 'correct way'. At the end of the day, replacing a task can be just
removing it and adding it back. I must finish this program ASAP to continue doing DDBB
"""


def change_task():
    try:
        index = int(
            input(
                f"{YELLOW_COLOR}[+] En la parte superior tienes el número de cada tarea{RESET_COLOR}\n"
                "Introduce número de tarea a cambiar: "
            )
        )

        real_index = index - 1

        if real_index < 0 or real_index >= len(tasks):
            print(f"{RED_COLOR}El índice no existe en la lista de tareas.{RESET_COLOR}")
            return

        # Eliminamos la tarea existente
        tasks.pop(real_index)

        # Añadir nueva tarea usando tu función ya existente
        add_task()

    except ValueError:
        print(
            f"{RED_COLOR}Introduce un índice como 1, 2, 3... No otro tipo de valor.{RESET_COLOR}"
        )


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
                    os.system("clear")  #! Won't work on the old Windows CMD
                    add_task()
                except ValueError:  # ? Does this except actually catch anything?
                    print("Porfavor, escribe una tarea y su estado, no numeros")
            case 2:
                os.system("clear")
                display_tasks()
            case 3:
                os.system("clear")
                display_tasks()
                print(f"{BLUE_COLOR}--- ACCIONES ---{RESET_COLOR}")
                print(
                    f"{BLUE_COLOR}[1]{RESET_COLOR} Cambiar nombre y estado de una tarea"
                )
                print(f"{BLUE_COLOR}[2]{RESET_COLOR} Eliminar tarea")

                print(f"{BLUE_COLOR}[3]{RESET_COLOR} Volver hacia atras")
                try:
                    to_do = int(input("Opcion a realizar (numero): "))
                    match to_do:
                        case 1:
                            display_tasks()
                            change_task()
                        case 2:
                            remove_task()
                        case 3:
                            continue
                except ValueError:
                    print(
                        f"{RED_COLOR} Debes introducir 1, 2 o 3 como acción!{RESET_COLOR}"
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
