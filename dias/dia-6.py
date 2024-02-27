# Día 6: Acceso seguro
# Este código solicita al usuario un nombre de usuario y una contraseña, y luego verifica si son correctos para permitir el acceso.

# Muestra un mensaje de bienvenida
print("Acceso seguro")

# Solicita al usuario su nombre de usuario y contraseña
username = input("¿Cuál es tu nombre de usuario?")
password = input("¿Cuál es tu contraseña?")

# Verifica si el nombre de usuario y la contraseña coinciden con las combinaciones permitidas
if username == "cristian" and password == "1234":
    print("¡Bienvenido Cristian! ¡Te ves bien hoy!")
elif username == "Lala" and password == "1234":
    print("Hola Lala! ¡Amo tu cabello hoy!")
elif username == "Bill" and password == "1234":
    print("¡Oye! Bill! ¡¿Qué pasa?!")
else:
    print("No tienes acceso.")
