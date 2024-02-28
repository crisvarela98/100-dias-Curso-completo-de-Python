import os
import time

# Lista de tareas pendientes
listaDeTareas = []

# Función para imprimir la lista de tareas
def imprimirLista():
    print()
    for tarea in listaDeTareas:
        print(tarea)
    print()

# Bucle principal del programa
while True:
    menu = input("Administrador de Lista de Tareas\n¿Deseas ver, agregar, editar, eliminar o borrar la lista de tareas pendientes?\n")
    if menu == "ver":
        imprimirLista()
    elif menu == "agregar":
        item = input("¿Qué tarea deseas agregar?\n").capitalize()  # Capitalizar la primera letra
        listaDeTareas.append(item)
    elif menu == "eliminar":
        item = input("¿Qué tarea deseas eliminar?\n").capitalize()  # Capitalizar la primera letra
        confirmacion = input("¿Estás seguro de que deseas eliminar esto?\n")
        if confirmacion[0].lower() == "s":  # Si la respuesta comienza con 's' (sí)
            if item in listaDeTareas:
                listaDeTareas.remove(item)
    elif menu == "editar":
        item = input("¿Qué tarea deseas editar?\n").capitalize()  # Capitalizar la primera letra
        nueva_tarea = input("¿A qué deseas cambiarlo?\n").capitalize()  # Capitalizar la primera letra
        for i in range(len(listaDeTareas)):
            if listaDeTareas[i] == item:
                listaDeTareas[i] = nueva_tarea
    elif menu == "borrar":
        listaDeTareas = []  # Borrar todas las tareas
    time.sleep(1)
    os.system('clear')  # Limpiar la pantalla
