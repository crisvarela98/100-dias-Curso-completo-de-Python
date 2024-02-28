import os
import time

# Lista de tareas pendientes
toDoList = []

# Función para imprimir la lista de tareas
def printList():
    print()
    for item in toDoList:
        print(item)
    print()

# Función para imprimir un título con color
def printColorTitle(title, color_code):
    print(f"\033[{color_code}m{title}\033[0m")

# Bucle principal del programa
while True:
    # Menú principal
    menu = input("\nAdministrador de Lista de Tareas\n\n¿Deseas ver, agregar o editar la lista de tareas pendientes? (Escribe 'exit' para salir)\n")

    # Ver la lista de tareas
    if menu == "ver":
        printList()

    # Agregar una nueva tarea
    elif menu == "agregar":
        item = input("¿Qué tarea deseas agregar?\n")
        toDoList.append(item)

    # Editar la lista de tareas
    elif menu == "editar":
        item = input("¿Qué tarea deseas eliminar?\n")
        if item in toDoList:
            toDoList.remove(item)

    # Salir del programa
    elif menu == "exit":
        printColorTitle("¡Hasta luego! Gracias por usar el Administrador de Lista de Tareas.", "32")  # 32 es el código de color verde
        break
