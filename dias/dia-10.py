# Define una función para calcular el monto de propina.
def calculate_tip_amount(bill, tip_percentage):
    tip_amount = bill * (tip_percentage / 100)
    return tip_amount

# Función principal que maneja la entrada del usuario y calcula la cuenta total y la cantidad a pagar por persona.
def main():
    try:
        # Solicita al usuario ingresar la cuenta, el número de personas y el porcentaje de propina.
        my_bill = float(input("¿Cuál fue la cuenta?: "))
        number_of_people = int(input("¿Cuántas personas son?: "))
        tip_percentage = int(input("¿Qué porcentaje de propina desea dejar? (Ingrese el valor numérico): "))

        # Validamos que el porcentaje de propina sea un valor común (15, 18, o 20 por ciento).
        if tip_percentage not in [15, 18, 20]:
            print("Por favor, ingrese un porcentaje de propina válido: 15, 18, o 20 por ciento.")
            return

        # Calcula el monto de la propina, la cuenta total y la cantidad a pagar por persona.
        tip_amount = calculate_tip_amount(my_bill, tip_percentage)
        total_bill = my_bill + tip_amount
        bill_per_person = total_bill / number_of_people

        # Imprime la cuenta total y la cantidad a pagar por persona.
        print(f"La cuenta total, incluyendo propina, es: {total_bill:.2f}")
        print(f"Cada persona debe pagar: {bill_per_person:.2f}")

    except ValueError:
        print("Ha ocurrido un error. Por favor, asegúrese de ingresar valores numéricos válidos.")

# Se llama a la función main cuando el script se ejecuta directamente.
if __name__ == "__main__":
    main()
