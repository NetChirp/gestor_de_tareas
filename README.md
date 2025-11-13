## 📝 Gestor de Tareas Pendientes (To-Do List) en Python

Este repositorio contiene un script simple en Python diseñado para gestionar una lista de tareas pendientes (To-Do List) a través de una interfaz de consola.

---

## ✨ Características

El objetivo de este programa es permitir a los usuarios gestionar una lista de tareas pendientes. El programa debe permitir:

* **Agregar Tarea**: Esta opción permitirá al usuario ingresar una nueva tarea y la agrega a la lista de tareas pendientes.
* **Listar Tareas**: Muestra una lista numerada de todas las tareas pendientes, indicando si están completadas o no.
* **Marcar Tarea como Completada**: Permite al usuario seleccionar una tarea de la lista y marcarla como completada.
* **Eliminar Tarea**: Permite al usuario seleccionar una tarea de la lista y eliminarla de la lista de tareas.
* **Salir**: Termina el programa.

---

## 🛠️ Requerimientos Técnicos

El programa está implementado bajo las siguientes especificaciones:

* **Estructura de Datos**: El programa debe utilizar una lista para almacenar las tareas.
* **Representación de Tareas**: Cada tarea debe ser un diccionario con dos claves: "tarea" y "completada". Y esta debe ser almacenada en la lista 
* **Flujo del Programa**:
    * Se debe implementar un bucle `while` para mostrar el menú principal y permitir que el usuario seleccione una opción.
    * Cuando el usuario elija "Salir" en el menú, el programa debe mostrar un mensaje de despedida y finalizar.
    * Cada vez que el usuario elija una opción del menú, el programa debe llamar a la función correspondiente para llevar a cabo esa operación.
* **Manejo de Errores**:
    * Asegúrate de que el programa maneje adecuadamente las entradas de usuario incorrectas o inválidas.
    * Si no hay tareas pendientes, no permitir acceder a la opción de eliminar tareas o marcar tareas cómo completadas.
    * Si no hay tareas pendientes, debe salir un mensaje de que no hay tareas pendientes.

---

## 🚀 Uso

Para ejecutar el programa, simplemente corre el script de Python en tu terminal:

#### Windows
```bash
python main.py
```
#### Linux / MacOS:
```bash
python3 main.py
```
