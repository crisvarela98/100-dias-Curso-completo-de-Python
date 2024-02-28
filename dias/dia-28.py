import random, os, time

def rollDice(lado):
    """Función para simular el lanzamiento de un dado."""
    resultado = random.randint(1, lado)
    return resultado

def salud():
    """Función para generar el atributo de salud."""
    statSalud = ((rollDice(6) * rollDice(12)) / 2) + 10
    return statSalud

def fuerza():
    """Función para generar el atributo de fuerza."""
    statFuerza = ((rollDice(6) * rollDice(8)) / 2) + 12
    return statFuerza

# Inicio de la batalla
print("⚔️ ¡ES HORA DE LA BATALLA! ⚔️")
print()
nombreLeyenda1 = input("Nombre de tu Leyenda:\n")
tipoLeyenda1 = input("Tipo de Personaje (Humano, Elfo, Mago, Orco):\n")
print()
print(nombreLeyenda1)
saludLeyenda1 = salud()
fuerzaLeyenda1 = fuerza()
print("SALUD:", saludLeyenda1)
print("FUERZA:", fuerzaLeyenda1)
print()
print("¿Contra quién se enfrentará?")
print()

nombreLeyenda2 = input("Nombre de tu Leyenda:\n")
tipoLeyenda2 = input("Tipo de Personaje (Humano, Elfo, Mago, Orco):\n")
print()
print(nombreLeyenda2)
saludLeyenda2 = salud()
fuerzaLeyenda2 = fuerza()
print("SALUD:", saludLeyenda2)
print("FUERZA:", fuerzaLeyenda2)
print()

ronda = 1
ganador = None

while True:
    time.sleep(1)
    os.system("clear")
    print("⚔️ ¡ES HORA DE LA BATALLA! ⚔️")
    print()
    print("¡Comienza la batalla!")

    dadoLeyenda1 = rollDice(6)
    dadoLeyenda2 = rollDice(6)

    diferencia = abs(fuerzaLeyenda1 - fuerzaLeyenda2) + 1

    if dadoLeyenda1 > dadoLeyenda2:
        saludLeyenda2 -= diferencia
        if ronda == 1:
            print(nombreLeyenda1, "gana el primer golpe")
        else:
            print(nombreLeyenda1, "gana la ronda", ronda)
    elif dadoLeyenda2 > dadoLeyenda1:
        saludLeyenda1 -= diferencia
        if ronda == 1:
            print(nombreLeyenda2, "gana el primer golpe")
        else:
            print(nombreLeyenda2, "gana la ronda", ronda)
    else:
        print("Sus espadas chocan y empatan en la ronda", ronda)

    print()
    print(nombreLeyenda1)
    print("SALUD:", saludLeyenda1)
    print()
    print(nombreLeyenda2)
    print("SALUD:", saludLeyenda2)
    print()

    if saludLeyenda1 <= 0:
        print(nombreLeyenda1, "ha muerto!")
        ganador = nombreLeyenda2
        break
    elif saludLeyenda2 <= 0:
        print(nombreLeyenda2, "ha muerto!")
        ganador = nombreLeyenda1
        break
    else:
        print("Y ambos siguen de pie para la próxima ronda")
        ronda += 1

time.sleep(1)

print("⚔️ ¡ES HORA DE LA BATALLA! ⚔️")
print()
print(ganador, "ha ganado en", ronda, "rondas")
