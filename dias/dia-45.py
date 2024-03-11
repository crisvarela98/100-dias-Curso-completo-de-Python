import os
import time

# Lista de tareas por hacer
todo = []

# Función para agregar una nueva tarea
def agregar():
    time.sleep(1)
    os.system("clear")
    nombre = input("Nombre > ")
    fecha_limite = input("Fecha de vencimiento > ")
    prioridad = input("Prioridad > ").capitalize()
    fila = [nombre, fecha_limite, prioridad]
    todo.append(fila)
    print("Agregado")

# Función para ver las tareas
def ver():
    time.sleep(1)
    os.system("clear")
    opciones = input("1: Todas\n2: Por Prioridad\n> ")
    if opciones == "1":
        for fila in todo:
            for item in fila:
                print(item, end=" | ")
            print()
        print()
    else:
        prioridad = input("¿Qué prioridad? > ").capitalize()
        for fila in todo:
            if prioridad in fila:
                for item in fila:
                    print(item, end=" | ")
                print()
        print()
    time.sleep(1)

# Función para editar una tarea
def editar():
    time.sleep(1)
    os.system("clear")
    buscar = input("Nombre de la tarea a editar > ")
    encontrado = False
    for fila in todo:
        if buscar in fila:
            encontrado = True
    if not encontrado:
        print("No se pudo encontrar esa tarea")
        return
    for fila in todo:
        if buscar in fila:
            todo.remove(fila)
    nombre = input("Nombre > ")
    fecha_limite = input("Fecha de vencimiento > ")
    prioridad = input("Prioridad > ").capitalize()
    fila = [nombre, fecha_limite, prioridad]
    todo.append(fila)
    print("Agregado")

# Función para eliminar una tarea
def eliminar():
    time.sleep(1)
    os.system("clear")
    buscar = input("Nombre de la tarea a eliminar > ")
    for fila in todo:
        if buscar in fila:
            todo.remove(fila)

# Bucle principal del programa
while True:
    menu = input("1: Agregar\n2: Ver\n3: Editar\n4: Eliminar\n5: Salir\n> ")
    if menu == "1":
        agregar()
    elif menu == "2":
        ver()
    elif menu == "3":
        editar()
    elif menu == "4":
        eliminar()
    elif menu == "5":
        break

    time.sleep(1)
    os.system("clear")
