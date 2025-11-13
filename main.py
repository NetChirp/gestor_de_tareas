# Programa monolitico para la gestión de tareas

# Variables globales
execute: bool = True
tasks = []  # La lista donde se almacenaran las tareas
COLOR_ROJO = "\033[1;31;40m"
COLOR_RESET = "\033[0m"
COLOR_AZUL = "\033[1;34m"


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
    print(f"{COLOR_AZUL}OPCIONES{COLOR_RESET}")
    print(f"{COLOR_AZUL}[1]{COLOR_RESET} Añadir una nueva tarea")
    print(f"{COLOR_AZUL}[2]{COLOR_RESET} Consultar o gestionar tareas")
    print(f"{COLOR_AZUL}[3]{COLOR_RESET} Salir del programa")
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
                print(f"{COLOR_ROJO}Caso no esperado!{COLOR_RESET}")
    except ValueError:  # Si no es un entero
        print(
            f"{COLOR_ROJO}El valor introducido no es un numero. Introduce un numero del menu de opciones{COLOR_RESET}\n"
        )
