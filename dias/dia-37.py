print("GENERADOR DE NOMBRES DE STAR WARS")

# Solicitar al usuario que ingrese su primer nombre, apellido, el apellido de soltera de su madre y la ciudad en la que nació
todos = input("Ingresa tu primer nombre, apellido, apellido de soltera de tu mamá y la ciudad en la que naciste: ").split()

primer_nombre = todos[0].strip()
apellido = todos[1].strip()
apellido_madre = todos[2].strip()
ciudad = todos[3].strip()

# Generar el nombre de Star Wars utilizando partes de la entrada del usuario
nombre = f"{primer_nombre[:3].title()}{apellido[:3].lower()} {apellido_madre[:2].title()}{ciudad[-3:].lower()}"

# Mostrar el nombre de Star Wars generado
print(f"Tu nombre de Star Wars es: {nombre}")
