import random

bingo = []

# Función para generar un número aleatorio entre 1 y 90
def generar_numero():
    numero = random.randint(1, 90)
    return numero

# Función para imprimir de manera legible la matriz del bingo
def imprimir_carton():
    for fila in bingo:
        print(fila)

numeros = []

# Generar 8 números aleatorios y almacenarlos en una lista
for i in range(8):
    numeros.append(generar_numero())

# Ordenar la lista de números generados
numeros.sort()

# Crear la matriz del bingo con los números generados y la palabra "BINGO"
bingo = [[numeros[0], numeros[1], numeros[2]],
         [numeros[3], "BINGO", numeros[4]],
         [numeros[5], numeros[6], numeros[7]]
        ]

# Imprimir la matriz del bingo
imprimir_carton()
