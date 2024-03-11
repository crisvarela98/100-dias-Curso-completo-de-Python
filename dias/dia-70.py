import os

# Definir las variables de entorno directamente en el script
os.environ['adminUsername'] = 'cris123'
os.environ['adminPassword'] = 'cris123'

while True:
    # Solicitar al usuario el nombre de usuario y la contraseña
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    # Verificar si las credenciales coinciden con las del administrador
    if username == os.environ['adminUsername'] and password == os.environ['adminPassword']:
        print("¡Bienvenido Administrador!")
        break
    else:
        print("Inténtalo de nuevo")
