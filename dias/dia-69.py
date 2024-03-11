import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Novela Visual")
ventana.geometry("400x400")

# Historia inicial
historia = "Te encuentras con una mujer en camino a una reunión de Replit IRL"

# Funciones para los botones
def preguntarCodigo():
    global historia
    canvas.itemconfig(contenedor, image=codes)
    historia = "Ella intenta sacar su computadora portátil y la deja caer al suelo"
    etiquetaHistoria["text"] = historia
    boton1.pack_forget()
    boton2.pack_forget()
    boton3.pack()
    boton4.pack()

def contarReplit():
    global historia
    canvas.itemconfig(contenedor, image=replit)
    historia = "¿Por qué uso Replit, por supuesto, como todo individuo cuerdo!"
    etiquetaHistoria["text"] = historia
    boton1.pack_forget()
    boton2.pack_forget()
    boton5.pack()
    boton6.pack()

def editar():
    global historia
    canvas.itemconfig(contenedor, image=vs)
    historia = "Pasa dos horas cargando un editor de código\ny haciéndolo funcionar, tú esperas educadamente"
    etiquetaHistoria["text"] = historia
    boton3.pack_forget()
    boton4.pack_forget()
    botonReiniciar.pack()

def usar():
    global historia
    canvas.itemconfig(contenedor, image=amazing)
    historia = "Ambos celebran usando la mejor\n plataforma de codificación en camino a la reunión"
    etiquetaHistoria["text"] = historia
    boton3.pack_forget()
    boton4.pack_forget()
    botonReiniciar.pack()

def tambien():
    global historia
    canvas.itemconfig(contenedor, image=days)
    historia = "¡Te cuenta todo sobre los 100 días de código!"
    etiquetaHistoria["text"] = historia
    boton5.pack_forget()
    boton6.pack_forget()
    botonReiniciar.pack()

def ganar():
    global historia
    canvas.itemconfig(contenedor, image=amazing)
    historia = "Ambos celebran usando la mejor\n plataforma de codificación en camino a la reunión\ny hablan sobre los 100 días de código"
    etiquetaHistoria["text"] = historia
    boton5.pack_forget()
    boton6.pack_forget()
    botonReiniciar.pack()

def reiniciar():
    global historia
    canvas.itemconfig(contenedor, image=comienzo)
    historia = "Te encuentras con una mujer en camino a una reunión de Replit IRL"
    etiquetaHistoria["text"] = historia
    botonReiniciar.pack_forget()
    boton1.pack()
    boton2.pack()

# Cargar imágenes
comienzo = tk.PhotoImage(file="archivos/69/1.png")
comienzo = comienzo.subsample(4)
codes = tk.PhotoImage(file="archivos/69/3.png")
codes = codes.subsample(4)
replit = tk.PhotoImage(file="archivos/69/2.png")
replit = replit.subsample(4)
days = tk.PhotoImage(file="archivos/69/4.png")
days = days.subsample(4)
amazing = tk.PhotoImage(file="archivos/69/5.png")
amazing = amazing.subsample(4)
vs = tk.PhotoImage(file="archivos/69/6.png")
vs = vs.subsample(4)

# Crear canvas para las imágenes
canvas = tk.Canvas(ventana, width=300, height=200)
canvas.pack()
contenedor = canvas.create_image(150, 150, image=comienzo)

# Etiqueta para mostrar la historia
etiquetaHistoria = tk.Label(text=historia)
etiquetaHistoria.pack()

# Botones
boton1 = tk.Button(text="¿Preguntarle cómo programa?", command=preguntarCodigo)
boton1.pack()

boton2 = tk.Button(text="Contarle sobre Replit", command=contarReplit)
boton2.pack()

boton3 = tk.Button(text="Ella dice 'Uso un editor local'", command=editar)
boton4 = tk.Button(text="Ella dice 'Uso Replit'", command=usar)
boton5 = tk.Button(text="Tú dices 'Yo también uso Replit'", command=tambien)
boton6 = tk.Button(text="Tú dices 'Actualmente estoy haciendo los 100 días de código'", command=ganar)
botonReiniciar = tk.Button(text="Reiniciar", command=reiniciar)

# Iniciar el bucle principal de la interfaz gráfica
tk.mainloop()
