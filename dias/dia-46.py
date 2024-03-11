import os, time

# Diccionario para almacenar la información de las bestias
mokedex = {}

# Función para imprimir de manera legible la información de las bestias
def prettyPrint():
    print(f"Nombre\tTipo\tHP\tMP")
    for key, value in mokedex.items():
        print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

# Bucle principal del programa
while True:
    print("¡Agrega tu Bestia!")
    nombre = input("Nombre > ").title()
    tipo = input("Tipo > ").title()
    hp = int(input("HP > "))
    mp = int(input("MP > "))
    # Agregar la bestia al diccionario mokedex
    mokedex[nombre] = { "type": tipo, "hp": hp, "mp": mp}
    print("----------")
    print()
    # Imprimir la información actualizada de todas las bestias
    prettyPrint()
