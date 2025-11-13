# Programa monolitico para la gestión de tareas

# Variables globales
execute: bool = True
tasks = []

""" 
Estructura esperada de tasks: 

tasks = [(tarea1), (estado) # Indice 0 y 1, (tarea2), (estado) # Indice 2 y 3]
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
    for task_item in tasks:
        # task_item is the full task (e.g., ('Comprar leche', 'Pendiente'))
        task_name = task_item[0]  # Get the name only

        if task_name.lower() == name.lower():
            print(
                f"{YELLOW_COLOR}La tarea ya existe! Por favor, introduce otro nombre.{RESET_COLOR}\n"
            )
            return True  # Tarea existe

    return False  # Tarea no existe


def add_task(name: str, status: str):
    pass


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
                    task_to_add: str = input("[+] Introduce la tarea: ")
                    status_of_task: str = input(
                        "[+] Introduce el estado de la tarea (Completada o Pendiente): "
                    )
                except ValueError:
                    print("El valor introducido no es del")
            case 2:
                pass
            case 3:
                execute = False
                break
            case _:  # Caso que se ejecutara si ninguno de los anteriores es valido
                print(f"{RED_COLOR}Caso no esperado!{RESET_COLOR}")
    except ValueError:  # Si no es un entero
        print(
            f"{RED_COLOR}El valor introducido no es un numero. Introduce un numero del menu de opciones{RESET_COLOR}\n"
        )
