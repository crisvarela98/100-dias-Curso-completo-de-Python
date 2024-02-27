# Monto inicial del préstamo
prestamo = 1000

# Tasa de interés anual (APR)
tasa_interes = 0.05

# Bucle para calcular el saldo del préstamo durante 10 años
for i in range(10):
    # Calcula el saldo del préstamo para el año actual
    prestamo += (prestamo * tasa_interes)

    # Imprime el saldo del préstamo para el año actual
    print("El año", i+1, "es", round(prestamo, 2))
