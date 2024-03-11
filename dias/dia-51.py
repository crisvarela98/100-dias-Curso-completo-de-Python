print("VOLVER A HACER DIA 51")
print()
print("Traceback (most recent call last):"
       "File /home/runner/dias-51-a-60/dias/dia-51.py, line 8, in <module> with open(to.do, r) as archivo: FileNotFoundError: [Errno 2] No such file or directory: 'to.do'")

"""
import os
import time

# Inicializar la lista de tareas pendientes
todo = []

# Leer las tareas pendientes desde el archivo "to.do" y cargarlas en la lista
with open("to.do", "r") as archivo:
    contenido_archivo = archivo.read()
    if contenido_archivo:
        todo = eval(contenido_archivo)  # Convertir la cadena de texto en una lista

# Función para agregar una nueva tarea
def agregar():
    time.sleep(1)
    os.system("clear")
    # Solicitar información sobre la nueva tarea
    nombre = input("Nombre > ")
    fecha_limite = input("Fecha límite > ")
    prioridad = input("Prioridad > ").capitalize()
    # Crear una lista con los detalles de la tarea y agregarla a la lista de tareas pendientes
    tarea = [nombre, fecha_limite, prioridad]
    todo.append(tarea)
    print("Tarea agregada")

# Función para ver las tareas
def ver():
    time.sleep(1)
    os.system("clear")
    opciones = input("1: Todas\n2: Por prioridad\n> ")
    if opciones == "1":
        # Mostrar todas las tareas
        for tarea in todo:
            print(" | ".join(tarea))
        print()
    else:
        # Mostrar tareas por prioridad
        prioridad = input("¿Qué prioridad? > ").capitalize()
        for tarea in todo:
            if prioridad in tarea:
                print(" | ".join(tarea))
        print()
    time.sleep(1)

# Función para editar una tarea
def editar():
    time.sleep(1)
    os.system("clear")
    nombre_tarea = input("Nombre de la tarea a editar > ")
    tarea_encontrada = False
    for tarea in todo:
        if nombre_tarea in tarea:
            tarea_encontrada = True
    if not tarea_encontrada:
        print("No se encontró esa tarea")
        return
    for tarea in todo:
        if nombre_tarea in tarea:
            todo.remove(tarea)
    nombre = input("Nombre > ")
    fecha_limite = input("Fecha límite > ")
    prioridad = input("Prioridad > ").capitalize()
    tarea = [nombre, fecha_limite, prioridad]
    todo.append(tarea)
    print("Tarea editada")

# Función para eliminar una tarea
def eliminar():
    time.sleep(1)
    os.system("clear")
    nombre_tarea = input("Nombre de la tarea a eliminar > ")
    for tarea in todo:
        if nombre_tarea in tarea:
            todo.remove(tarea)
    print("Tarea eliminada")

# Bucle principal del programa
while True:
    menu = input("1: Agregar\n2: Ver\n3: Editar\n4: Eliminar\n> ")
    if menu == "1":
        agregar()
    elif menu == "2":
        ver()
    elif menu == "3":
        editar()
    else:
        eliminar()

    time.sleep(1)
    os.system("clear")
    # Escribir la lista actualizada de tareas pendientes en el archivo "to.do"
    with open("to.do", "w") as archivo:
        archivo.write(str(todo))
"""