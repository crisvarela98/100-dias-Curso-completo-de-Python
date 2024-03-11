class personaje:
  nombre = None
  salud = 100
  mp = 100

  def __init__(self, nombre):
    self.nombre = nombre

  def imprimir(self):
    print(f"{self.nombre}\tHP: {self.salud}\t MP: {self.mp}")

  def establecerEstadisticas(self, salud, mp):
    self.salud = salud
    self.mp = mp

class jugador(personaje):
  apodo = None
  vidas = 3

  def __init__(self, apodo):
    self.nombre = "Jugador"
    self.apodo = apodo

  def imprimir(self):
    print(f"{self.nombre}\tHP: {self.salud}\t MP: {self.mp}\tApodo: {self.apodo}\tVidas: {self.vidas}")

  def estaVivo(self):
    if self.vidas > 0:
      print(f"¡{self.apodo} sigue vivo!")
      return True
    else:
      print(f"¡{self.apodo} ha expirado!")
      return False

ian = jugador("Ian el poderoso")
ian.imprimir()
print(ian.estaVivo())

class enemigo(personaje):
  tipo = None
  fuerza = None

  def __init__(self, nombre, tipo, fuerza):
    self.nombre = nombre
    self.tipo = tipo
    self.fuerza = fuerza

  def imprimir(self):
    print(f"{self.nombre}\tHP: {self.salud}\t MP: {self.mp}\tTipo: {self.tipo}\tFuerza: {self.fuerza}")

class orco(enemigo):
  velocidad = None

  def __init__(self, velocidad):
    self.nombre = "Orco"
    self.tipo = "Orco"
    self.fuerza = 200
    self.velocidad = velocidad

  def imprimir(self):
    print(f"{self.nombre}\tHP: {self.salud}\t MP: {self.mp}\tTipo: {self.tipo}\tFuerza: {self.fuerza}\tVelocidad: {self.velocidad}")

sharron = orco(250)
gary = orco(205)

sharron.imprimir()
gary.imprimir()

class vampiro(enemigo):
  dia = True

  def __init__(self, dia):
    self.nombre = "Vampiro"
    self.tipo = "Vampiro"
    self.fuerza = 150
    self.dia = dia

  def imprimir(self):
    print(f"{self.nombre}\tHP: {self.salud}\t MP: {self.mp}\tTipo: {self.tipo}\tFuerza: {self.fuerza}\tDía: {self.dia}")

eric = vampiro(False)
eric.imprimir()
