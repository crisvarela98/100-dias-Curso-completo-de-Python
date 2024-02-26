
print("Acceso seguro")
username = input("¿Cual es tu nombre de usuario?")
password = input("¿Cual es tu contraseña?")

if username == "cristian" and password == "1234":
  print("¡Bienvenido Cristian! ¡Te ves bien hoy!")
elif username == "Lala" and password == "1234":
  print("Hola Lala! ¡Amo tu cabello hoy!")
elif username == "Bill" and password == "1234":
  print("¡Oye! Bill! ¡¿Que pasa?!")
else:
  print("No tienes acceso.")