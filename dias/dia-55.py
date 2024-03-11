# | Nombre | Fecha | Prioridad
import os, time, random

# Inicializar una lista vacía para almacenar las tareas
todo = []

# Variable para verificar si el archivo existe
fileExists = True

# Intentar abrir el archivo "to.do" para cargar las tareas existentes
try:
    f = open("to.do", "r")
    todo = eval(f.read())  # Cargar las tareas desde el archivo y convertirlas en una lista
    f.close()
except:
    fileExists = False  # Si el archivo no existe, establecer fileExists en False

# Función para agregar una nueva tarea
def add():
    time.sleep(1)  # Hacer una pausa de 1 segundo
    os.system("clear")  # Limpiar la pantalla
    name = input("Nombre > ")
    date = input("Fecha de Vencimiento > ")
    priority = input("Prioridad > ").capitalize()  # Capitalizar la primera letra de la prioridad
    row = [name, date, priority]  # Crear una nueva fila de tarea
    todo.append(row)  # Agregar la fila a la lista de tareas
    print("Agregado")

# Función para ver las tareas
def view():
    time.sleep(1)
    os.system("clear")
    options = input("1: Todas\n2: Por Prioridad\n> ")
    if options == "1":
        for row in todo:
            for item in row:
                print(item, end=" | ")  # Imprimir cada elemento de la fila separado por "|"
            print()
        print()
    else:
        priority = input("¿Qué prioridad? > ").capitalize()
        for row in todo:
            if priority in row:
                for item in row:
                    print(item, end=" | ")
                print()
        print()
    time.sleep(1)

# Función para editar una tarea existente
def edit():
    time.sleep(1)
    os.system("clear")
    find = input("Nombre de la tarea a editar > ")
    found = False
    for row in todo:
        if find in row:
            found = True
    if not found:
        print("No se pudo encontrar la tarea")
        return
    for row in todo:
        if find in row:
            todo.remove(row)
    name = input("Nombre > ")
    date = input("Fecha de Vencimiento > ")
    priority = input("Prioridad > ").capitalize()
    row = [name, date, priority]
    todo.append(row)
    print("Agregado")

# Función para eliminar una tarea
def remove():
    time.sleep(1)
    os.system("clear")
    find = input("Nombre de la tarea a eliminar > ")
    for row in todo:
        if find in row:
            todo.remove(row)

# Bucle principal del programa
while True:
    menu = input("1: Agregar\n2: Ver\n3: Editar\n4: Eliminar\n> ")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    else:
        remove()

    time.sleep(1)
    os.system("clear")

    # Realizar una copia de seguridad de las tareas en un archivo de texto
    if fileExists:
        try:
            os.mkdir("backups")
        except:
            pass
        name = f"backup{random.randint(1, 1000000000)}.txt"
        os.popen(f"cp to.do backups/{name}")

    # Guardar las tareas en el archivo "to.do"
    f = open("to.do", "w")
    f.write(str(todo))  # Convertir la lista de tareas a una cadena y escribirla en el archivo
    f.close()
