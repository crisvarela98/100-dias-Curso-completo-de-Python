import os
import subprocess

# Función para imprimir un mensaje enmarcado con un color específico
def imprimir_mensaje_enmarcado(mensaje, color='\033[92m'):
    ancho = len(mensaje) + 4
    print(color + '¬' * ancho)
    print(f'  {mensaje}')
    print('¬' * ancho + '\033[0m')

# Función para imprimir un mensaje enmarcado con el color verde
def imprimir_mensaje_continuar(mensaje):
    # Utiliza la función imprimir_mensaje_enmarcado con el color verde (código de color 95)
    imprimir_mensaje_enmarcado(mensaje, color='\033[92m')
    # Espera a que el usuario presione Enter para continuar
    input()

def abrir_archivo_dia(numero_dia):
    # Construye el nombre del archivo a partir del número del día
    nombre_archivo = f'dia-{numero_dia}.py'
    # Construye la ruta completa del archivo a partir del nombre y el directorio 'dias'
    ruta_archivo = os.path.join('dias', nombre_archivo)

    try:
        # Pregunta al usuario si desea ejecutar el archivo
        imprimir_mensaje_enmarcado("¿Desea ejecutar este archivo? (s/n):")
        ejecutar = input().lower()
        if ejecutar == 's':
            subprocess.run(['python', ruta_archivo])
        else:
            # Pregunta al usuario si desea abrir el archivo
            imprimir_mensaje_enmarcado(f"¿Desea abrir el archivo {nombre_archivo}? (s/n):")
            abrir = input().lower()
            if abrir == 's':
                # Intenta abrir el archivo en modo lectura
                with open(ruta_archivo, 'r') as archivo:
                    # Lee el contenido del archivo
                    contenido = archivo.read()
                    # Imprime el contenido del archivo enmarcado
                    imprimir_mensaje_enmarcado(f"Contenido del archivo {nombre_archivo}")
                    print(contenido)

                    # Pregunta al usuario si desea modificar el archivo
                    imprimir_mensaje_enmarcado("¿Desea modificar este archivo? (s/n):")
                    modificar = input().lower()
                    if modificar == 's':
                        # Abre el archivo en modo escritura y permite al usuario modificarlo
                        with open(ruta_archivo, 'w') as archivo_modificado:
                            nuevo_contenido = input("Ingrese el nuevo contenido:\n")
                            archivo_modificado.write(nuevo_contenido)
    except FileNotFoundError:
        # Maneja el caso en que el archivo no se encuentra
        print(f"El archivo {nombre_archivo} no se encontró.")

if __name__ == "__main__":
    while True:
        # Limpia la consola para una mejor presentación
        os.system('cls' if os.name == 'nt' else 'clear')  
        # Imprime un mensaje enmarcado para que el usuario ingrese el número del día
        imprimir_mensaje_enmarcado("Ingrese el número del día del archivo que desea abrir (11-20)", '\033[92m')
        # Lee la entrada del usuario que indica el número del día
        numero_dia = input()
        # Llama a la función abrir_archivo_dia para abrir el archivo correspondiente al día indicado
        abrir_archivo_dia(numero_dia)
        # Muestra un mensaje y espera a que el usuario presione Enter para continuar
        imprimir_mensaje_continuar("Presione Enter para continuar...")
