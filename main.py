import os
import subprocess

# Función para imprimir un mensaje enmarcado con un color específico
def imprimir_mensaje_enmarcado(mensaje, color='\033[95m'):
    ancho = len(mensaje) + 4
    print(color + '=' * ancho)
    print(f'  {mensaje}')
    print('=' * ancho + '\033[0m')

# Función para imprimir un mensaje enmarcado con el color magenta
def imprimir_mensaje_continuar(mensaje):
    imprimir_mensaje_enmarcado(mensaje, '\033[95m')
    input()

def abrir_archivo_dia(numero_dia):
    nombre_archivo = f'dia-{numero_dia}.py'
    ruta_archivo = os.path.join('dias', nombre_archivo)

    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            imprimir_mensaje_enmarcado(f"Contenido del archivo {nombre_archivo}")
            print(contenido)
            # Ejecutar el archivo si se desea
            imprimir_mensaje_enmarcado("¿Desea ejecutar este archivo? (s/n):")
            ejecutar = input().lower()
            if ejecutar == 's':
                subprocess.run(['python', ruta_archivo])
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
        imprimir_mensaje_enmarcado("Ingrese el número del día del archivo que desea abrir (1-10)", '\033[95m')
        numero_dia = input()
        abrir_archivo_dia(numero_dia)
        imprimir_mensaje_continuar("Presione Enter para continuar...")
