# Importamos el módulo datetime para trabajar con fechas y horas
import datetime

# Obtenemos la fecha actual
hoy = datetime.date.today()

# Imprimimos un encabezado para el contador de eventos
print("CUENTA REGRESIVA PARA EL EVENTO")

# Solicitamos al usuario que ingrese la fecha del evento
dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

# Creamos un objeto de fecha para el evento utilizando la entrada del usuario
evento = datetime.date(año, mes, dia)

# Calculamos la diferencia entre la fecha del evento y la fecha actual
diferencia = evento - hoy

# Convertimos la diferencia en días
diferencia = diferencia.days

# Comprobamos si faltan días para el evento, si ya ocurrió, o si es hoy mismo
if diferencia > 0:
    # Mostramos cuántos días faltan para el evento
    print(f"¡Faltan {diferencia} días!")
elif diferencia < 0:
    # Mostramos un mensaje indicando que el evento ya pasó
    print(f"😭😭😭😭😭😭😭 ¡Lo perdiste por {-diferencia} días!")
else:
    # Si la diferencia es cero, entonces es el día del evento
    print("🥳🥳🥳🥳🥳🥳🥳 ¡Hoy es el día del evento!")
