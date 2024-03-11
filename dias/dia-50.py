import os, time, random

# Función para agregar una idea al archivo
def agregar():
    os.system("clear")
    idea = input("Idea > ")
    # Abrir el archivo "my.ideas" en modo de agregar
    archivo = open("my.ideas", "a+")
    # Escribir la idea en el archivo
    archivo.write(f"{idea}\n")
    # Cerrar el archivo después de escribir
    archivo.close()
    time.sleep(1)
    os.system("clear")

# Función para mostrar una idea aleatoria del archivo
def mostrar():
    os.system("clear")
    # Abrir el archivo "my.ideas" en modo lectura
    archivo = open("my.ideas", "r")
    # Leer todas las ideas del archivo y dividirlas en una lista
    ideas = archivo.read().split("\n")
    # Cerrar el archivo después de la lectura
    archivo.close()
    # Eliminar elementos vacíos de la lista de ideas
    ideas.remove("")
    # Elegir una idea aleatoria de la lista
    idea = random.choice(ideas)
    print(idea)
    time.sleep(2)
    os.system("clear")

# Bucle principal del programa
while True:
    menu = input("1: Agregar idea\n2: Mostrar una idea aleatoria\n> ")
    if menu == "1":
        agregar()
    else:
        mostrar()
