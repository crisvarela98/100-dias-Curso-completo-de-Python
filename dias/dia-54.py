# Importar el módulo csv para trabajar con archivos CSV
import csv

# Inicializar el total como un valor de punto flotante
total = 0.0

# Abrir el archivo CSV llamado "Day54Totals.csv" en modo lectura
with open("archivos/54/Day54Totals.csv") as archivo:
    # Crear un lector de diccionario CSV
    lector = csv.DictReader(archivo)

    # Iterar sobre cada fila del archivo CSV
    for fila in lector:
        # Calcular el costo total sumando la cantidad multiplicada por el costo de cada artículo
        total += float(fila["Quantity"]) * float(fila["Cost"])

# Imprimir el costo total redondeado a dos decimales
print(f"Total: ${round(total, 2)}")
