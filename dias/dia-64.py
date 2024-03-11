class trabajo:
  nombre = None
  salario = None
  horasTrabajadas = None

  def __init__(self, nombre, salario, horasTrabajadas):
    self.nombre = nombre
    self.salario = salario
    self.horasTrabajadas = horasTrabajadas

  def imprimir(self):
    print("== TRABAJO ==")
    print()
    print(f"{self.nombre:<10} {self.salario:^10} {self.horasTrabajadas:>10}")

class doctor(trabajo):
  experiencia = None
  especialidad = None

  def __init__(self, salario, horasTrabajadas, experiencia, especialidad):
    self.nombre = "Doctor"
    self.salario = salario
    self.horasTrabajadas = horasTrabajadas
    self.experiencia = experiencia
    self.especialidad = especialidad

  def imprimir(self):
    print("== TRABAJO ==")
    print()
    print(f"{self.nombre:<10} {self.salario:^10} {self.horasTrabajadas:>10}")
    print(f"{self.experiencia:<10} {self.especialidad:>21}")

class profesor(trabajo):
  materia = None
  puesto = None

  def __init__(self, salario, horasTrabajadas, materia, puesto):
    self.nombre = "Profesor"
    self.horasTrabajadas = horasTrabajadas
    self.salario = salario
    self.materia = materia
    self.puesto = puesto

  def imprimir(self):
    print("== TRABAJO ==")
    print()
    print(f"{self.nombre:<10} {self.salario:^10} {self.horasTrabajadas:>10}")
    print(f"{self.materia:<10} {self.puesto:>21}")

abogado = trabajo("Abogado", "$100,000", "40")
abogado.imprimir()

doc = doctor("$120,000", "48", "7", "Consultor Pediátrico")
doc.imprimir()

enseñar = profesor("$50,000", "48+", "Ciencias de la Computación", "Subdirector")
enseñar.imprimir()
