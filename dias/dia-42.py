# Definir un diccionario con claves para la información de MokéBeast y valores inicializados a None
mokedex = {"Nombre de la bestia": None, "Tipo": None, "Movimiento especial": None, "HP": None, "MP": None}

# Imprimir el título del programa
print("MokéBeast")
print()

# Solicitar al usuario que ingrese información sobre MokéBeast para cada clave del diccionario
for name, value in mokedex.items():
    mokedex[name] = input(f"{name}:\t").strip().title()

# Seleccionar el color del texto según el tipo de MokéBeast
if mokedex["Tipo"] == "Earth":
    print("\033[32m", end="")
elif mokedex["Tipo"] == "Air":
    print("\033[37m", end="")
elif mokedex["Tipo"] == "Fire":
    print("\033[31m", end="")
elif mokedex["Tipo"] == "Water":
    print("\033[34m", end="")
else:
    print("\033[33m", end="")

# Imprimir la información de MokéBeast con el color seleccionado
for name, value in mokedex.items():
    print(f"{name:<15}: {value}")
