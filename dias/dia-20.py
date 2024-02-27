# Mensaje de bienvenida al generador de lista de números
print("Bienvenido al generador de listas de números.")
print()
print("Vas a darme un número con el que quieras comenzar, un número final y cuánto quieres que añada cada vez.")
print()

# Solicita al usuario los números de inicio, fin y el incremento
inicio = int(input("¿Con qué número quieres comenzar? "))
fin = int(input("¿Con qué número quieres terminar? "))
incremento = int(input("¿Cuánto debo añadir cada vez? "))

# Bucle para generar la lista de números
for i in range(inicio, fin, incremento):
    print(i)  # Imprime cada número en la lista
