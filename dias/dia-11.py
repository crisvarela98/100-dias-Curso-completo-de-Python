# Solicita al usuario que ingrese el número de días en este año
dias_de_este_año = int(input("¿Cuántos días tiene este año?"))

# Definición de variables constantes
dias_en_año = 365
dias_en_año_bisiesto = 366
horas_en_día = 24
minutos_en_hora = 60
segundos_en_minuto = 60

# Calcula el total de segundos en un año no bisiesto
resultado = dias_en_año * horas_en_día * minutos_en_hora * segundos_en_minuto

# Calcula el total de segundos en un año bisiesto
resultado_año_bisiesto = dias_en_año_bisiesto * horas_en_día * minutos_en_hora * segundos_en_minuto

# Verifica si el año proporcionado por el usuario es bisiesto
if dias_de_este_año == 366:
    # Si es bisiesto, imprime el número de segundos en un año bisiesto
    print("El número de segundos en un año bisiesto es", resultado_año_bisiesto)
else:
    # Si no es bisiesto, imprime el número de segundos en un año no bisiesto
    print("El número de segundos en un año es", resultado)