import os, time

# Inicializar la lista de inventario
inventory = []

# Intentar cargar los datos del inventario desde el archivo "inventory.txt"
try:
    with open("inventory.txt", "r") as archivo:
        contenido_archivo = archivo.read()
        if contenido_archivo:
            inventory = eval(contenido_archivo)  # Convertir la cadena de texto en una lista
except FileNotFoundError:
    pass

# Función para agregar un elemento al inventario
def addItem():
    time.sleep(1)
    os.system("clear")
    print("INVENTARIO")
    print("=========")
    print()
    item = input("Elemento para agregar > ").capitalize()
    inventory.append(item)
    print("Agregado")

# Función para ver los elementos del inventario
def viewItem():
    time.sleep(1)
    os.system("clear")
    print("INVENTARIO")
    print("=========")
    print()
    seen = []
    for item in inventory:
        if item not in seen:
            print(f"{item} {inventory.count(item)}")
            seen.append(item)

    time.sleep(2)

# Función para eliminar un elemento del inventario
def removeItem():
    time.sleep(1)
    os.system("clear")
    print("INVENTARIO")
    print("=========")
    print()
    item = input("Elemento para eliminar > ").capitalize()
    if item in inventory:
        inventory.remove(item)
        print("Eliminado")
    else:
        print("No tienes ese elemento")

# Bucle principal del programa
while True:
    time.sleep(1)
    os.system("clear")
    print("INVENTARIO")
    print("=========")
    print()
    menu = input("1: Agregar\n2: Ver\n3: Eliminar\n4: Salir\n> ")
    if menu == "1":
        addItem()
    elif menu == "2":
        viewItem()
    elif menu == "3":
        removeItem()
    elif menu == "4":
        # Salir del bucle principal si se selecciona la opción de salir
        break

# Guardar los datos del inventario en el archivo "inventory.txt"
with open("inventory.txt", "w") as archivo:
    archivo.write(str(inventory))
