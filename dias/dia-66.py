import tkinter as tk

ventana = tk.Tk()  # Crea una ventana
ventana.title("Calculadora")  # Establece el título de la ventana
ventana.geometry("400x200")  # Establece las dimensiones de la ventana

respuesta = 0
ultimoNumero = 0
operador = None

# Función para ingresar números en la pantalla
def ingresarRespuesta(valor):
  global respuesta
  respuesta = f"{respuesta}{valor}"
  respuesta = int(respuesta)
  etiqueta["text"] = respuesta

# Función para realizar operaciones y seleccionar el operador
def calcularRespuesta(esteOp):
  global respuesta, ultimoNumero, operador
  ultimoNumero = respuesta
  respuesta = 0
  if esteOp == "+":
    operador = "+"
  elif esteOp == "-":
    operador = "-"
  elif esteOp == "*":
    operador = "*"
  elif esteOp == "/":
    operador = "/"
  etiqueta["text"] = respuesta

# Función para realizar el cálculo final
def calcular():
  global respuesta, ultimoNumero, operador
  print(f"{ultimoNumero}\t{respuesta}\t{operador}")
  if operador == "+":
    total = ultimoNumero + respuesta
  elif operador == "-":
    total = ultimoNumero - respuesta
  elif operador == "*":
    total = ultimoNumero * respuesta
  elif operador == "/":
    total = ultimoNumero / respuesta
  respuesta = total
  etiqueta["text"] = respuesta

etiqueta = tk.Label(text=respuesta)  # Crea una etiqueta para mostrar los números ingresados y el resultado
etiqueta.grid(row=0, column=1)  # Ubica la etiqueta en la fila 0 y la columna 1

# Crea botones para los números del 0 al 9
for i in range(1, 10):
    boton = tk.Button(text=str(i), command=lambda i=i: ingresarRespuesta(i))
    boton.grid(row=(i-1)//3 + 1, column=(i-1)%3)

# Crea botones para las operaciones de suma, resta, multiplicación y división
operadores = ["+", "-", "*", "/"]
for i, operador in enumerate(operadores):
    boton = tk.Button(text=operador, command=lambda operador=operador: calcularRespuesta(operador))
    boton.grid(row=i+1, column=4)

# Crea un botón para la igualdad
igual = tk.Button(text="=", command=calcular)
igual.grid(row=4, column=4)

tk.mainloop()  # Ejecuta el bucle principal de la interfaz gráfica
