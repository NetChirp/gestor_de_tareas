# Programa monolitico para la gestión de tareas

# Variables globales
execute: bool = True
tasks = []  # La lista donde se almacenaran las tareas
RED_COLOR = "\033[1;31;40m"
RESET_COLOR = "\033[0m"
BLUE_COLOR = "\033[1;34m"


def search_task(name):
    for counter in tasks:
        if tasks[counter] == name:
            print("La tarea ya existe!")
        else:
            counter += 1
    pass


def add_task(name, status):

    pass


def remove_task(name):
    pass


def change_task_status(name, new_status):
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
                task_to_add = input("[+] Introduce la tarea: ")
                status_of_task = input(
                    "[+] Introduce el estado de la tarea (Completada o Pendiente): "
                )
                add_task(task_to_add, status_of_task)
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
