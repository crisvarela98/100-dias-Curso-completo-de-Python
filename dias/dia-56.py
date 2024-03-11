import csv
import os
from colorama import init, Fore

# Inicializar colorama para usar los colores en la consola
init(autoreset=True)

# Mensaje de estado
print(Fore.YELLOW + "Procesando la lista de las 100 canciones más reproducidas...")

# Directorio donde se encuentra el archivo CSV
csv_directory = "archivos/56"
csv_file = "100MostStreamedSongs.csv"

# Verificar si el directorio existe
if not os.path.exists(csv_directory):
    print(Fore.RED + f"Error: No se encontró el directorio '{csv_directory}'.")
    exit()

# Ruta completa al archivo CSV
csv_path = os.path.join(csv_directory, csv_file)

# Verificar si el archivo CSV existe
if not os.path.isfile(csv_path):
    print(Fore.RED + f"Error: No se encontró el archivo '{csv_file}' en '{csv_directory}'.")
    exit()

# Preguntar al usuario por el nombre del artista
artist_name = input(Fore.CYAN + "Ingrese el nombre del artista cuyas canciones desea descargar: ").strip().title()

# Mensaje de estado
print(Fore.YELLOW + f"Descargando canciones de {artist_name}...")

# Abrir el archivo CSV que contiene la lista de las 100 canciones más reproducidas
with open(csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # Crear un lector de diccionario para el archivo CSV

    # Iterar sobre cada fila del archivo CSV
    for row in reader:
        artist = row["Artist(s)"].title()  # Obtener el nombre del artista y capitalizarlo
        song = row["Song"]  # Obtener el nombre de la canción

        # Verificar si el artista coincide con el ingresado por el usuario
        if artist == artist_name:
            # Mensaje de estado
            print(Fore.CYAN + f"Procesando canción: {song} de {artist}")

            # Verificar si el directorio del artista no existe
            artist_directory = os.path.join(csv_directory, artist)
            if not os.path.exists(artist_directory):
                os.mkdir(artist_directory)  # Crear un directorio para el artista si no existe

            # Construir la ruta del archivo de la canción
            song_path = os.path.join(artist_directory, song + ".txt")

            # Verificar si el archivo de la canción ya existe
            if os.path.exists(song_path):
                print(Fore.YELLOW + f"El archivo '{song}.txt' ya existe en '{artist}'.")
            else:
                # Crear un archivo para la canción en modo escritura
                with open(song_path, mode='w', encoding='utf-8') as f:
                    # Escribir un mensaje en el archivo
                    f.write("Letra de la canción, información adicional, etc.")

                print(Fore.GREEN + f"Se ha creado el archivo '{song}.txt' en '{artist}'.")

print(Fore.GREEN + "¡Proceso completado exitosamente!")
