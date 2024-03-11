# Definir un diccionario con claves de información de un sitio web y valores inicializados a None
website = {"name": None, "url": None, "desc": None, "rating": None}

# Solicitar al usuario que ingrese información sobre el sitio web para cada clave del diccionario
for name in website.keys():
    website[name] = input(f"{name}: ")

# Imprimir un espacio en blanco para separar las entradas del usuario y la salida del programa
print()

# Iterar sobre las claves y valores del diccionario e imprimir la información ingresada por el usuario
for name, value in website.items():
    print(f"{name}: {value}")

