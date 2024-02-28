rolodex = []

def imprimirLista():
    print()
    for nombre in rolodex:
        print(nombre)
    print()

while True:
    primerNombre = input("Primer Nombre: ").strip().capitalize()
    apellido = input("Apellido: ").strip().capitalize()
    nombre = f"{primerNombre} {apellido}"
    if nombre not in rolodex:
        rolodex.append(nombre)
    else:
        print("ERROR: Nombre duplicado")
    imprimirLista()
