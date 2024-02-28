import random, os, time

def rollDice(lados):
    """Función para simular el lanzamiento de un dado."""
    resultado = random.randint(1, lados)
    return resultado

def salud():
    """Función para generar el atributo de salud."""
    saludStat = ((rollDice(6) * rollDice(12)) / 2) + 10
    return saludStat

def fuerza():
    """Función para generar el atributo de fuerza."""
    fuerzaStat = ((rollDice(6) * rollDice(8)) / 2) + 12
    return fuerzaStat

while True:
    print("⚔️ CONSTRUCTOR DE PERSONAJES ⚔️")
    print()
    nombre = input("Nombre de tu Leyenda:\n")
    tipo = input("Tipo de Personaje (Humano, Elfo, Mago, Orco):\n")
    print()
    print(nombre)
    print("SALUD:", salud())
    print("FUERZA:", fuerza())
    print()
    print("Que tu nombre pase a la Leyenda...")
    print()
    deNuevo = input("¿Otra vez?:\n")
    if deNuevo.lower() == "no":
        break
    time.sleep(1)
    os.system("clear")
