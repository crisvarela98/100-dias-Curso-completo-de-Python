# Solicitar información personal al usuario
nombre = input("Nombre: ").strip().capitalize()
fecha_nacimiento = input("Fecha de nacimiento: ").strip()
telefono = input("Número de teléfono: ").strip()
email = input("Correo electrónico: ")
direccion = input("Dirección: ")

# Crear un diccionario con la información proporcionada por el usuario
contacto = {"nombre": nombre, "fecha de nacimiento": fecha_nacimiento, "teléfono": telefono, "email": email, "dirección": direccion}

# Imprimir la información del contacto
print()
print(f"""Nombre: {contacto["nombre"]}""")
print(f"""Fecha de Nacimiento: {contacto["fecha de nacimiento"]}""")
print(f"""Teléfono: {contacto["teléfono"]}""")
print(f"""Correo Electrónico: {contacto["email"]}""")
print(f"""Dirección: {contacto["dirección"]}""")
