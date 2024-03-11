import os, time

# Abrir el archivo "high.score" en modo lectura
archivo = open("high.score", "r")

# Leer el contenido del archivo y dividirlo en líneas
puntuaciones = archivo.read().split("\n")

# Cerrar el archivo después de la lectura
archivo.close()

# Inicializar variables para el puntaje más alto y el nombre del jugador con el puntaje más alto
puntaje_maximo = 0
nombre_maximo = None

# Iterar sobre las puntuaciones
for fila in puntuaciones:
    # Dividir cada fila en datos (nombre y puntaje)
    datos = fila.split()
    # Verificar si la fila no está vacía
    if datos != []:
        # Convertir el puntaje a entero y compararlo con el puntaje máximo actual
        if int(datos[1]) > puntaje_maximo:
            # Actualizar el puntaje máximo y el nombre del jugador con el puntaje máximo
            puntaje_maximo = int(datos[1])
            nombre_maximo = datos[0]

# Imprimir al ganador y su puntaje más alto
print("El ganador es", nombre_maximo, "con", puntaje_maximo)
