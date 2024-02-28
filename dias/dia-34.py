import os
import time

# Lista de correos electrónicos
listaDeCorreos = []

# Función para imprimir la lista de correos electrónicos de forma legible
def imprimirLista():
    os.system("clear")  # Limpiar la pantalla
    print("Lista de Correos Electrónicos")
    print()
    contador = 1
    for correo in listaDeCorreos:
        print(f"{contador}: {correo}")
        contador += 1
    time.sleep(1)

# Función para enviar correos no deseados
def spam(max):
    for i in range(min(max, len(listaDeCorreos))):  # Usar el mínimo entre max y la longitud de listaDeCorreos
        print(f"""Correo {i+1}

Estimado(a) {listaDeCorreos[i]},
Hemos notado que te estás perdiendo de los increíbles 100 días de código en Replit. Te insistimos en que lo hagas de inmediato. Si no lo haces, pasaremos tu dirección de correo electrónico a cada remitente de correo no deseado que hayamos encontrado y también te inscribiremos en el boletín de My Little Pony, porque es genial. De todas formas, podríamos hacerlo.

Amor y abrazos,

Ian Spammington III""")
        time.sleep(1)
        os.system("clear")  # Limpiar la pantalla

# Bucle principal del programa
while True:
    print("SPAMMER Inc.")
    menu = input("1: Agregar correo electrónico\n2: Eliminar correo electrónico\n3: Mostrar correos electrónicos\n4: ¡A SPAMMEAR!\n> ")
    if menu == "1":
        correo = input("Correo electrónico > ")
        listaDeCorreos.append(correo)
    elif menu == "2":
        correo = input("Correo electrónico > ")
        if correo in listaDeCorreos:
            listaDeCorreos.remove(correo)
    elif menu == "3":
        imprimirLista()
    elif menu == "4":
        spam(10)  # Enviar 10 correos no deseados
    time.sleep(1)
    os.system("clear")  # Limpiar la pantalla
