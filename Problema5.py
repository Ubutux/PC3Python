"""
Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante.
"""

class Alumno:

  def __init__(self, nombre, numero_registro):

    self.nombre = nombre
    self.numero_registro = numero_registro
    self.edad = None
    self.notas = []

  def mostrar_informacion(self):

    print(f"Nombre: {self.nombre}")
    print(f"Número de registro: {self.numero_registro}")
    print(f"Edad: {self.edad}")
    print(f"Notas: {self.notas}")

  def set_edad(self, edad):

    self.edad = edad

  def set_notas(self, notas):

    self.notas = notas

def main():

  alumno = Alumno("Pepito", 12345)

  alumno.set_edad(20)

  alumno.set_notas([10, 9, 8, 7])

  alumno.mostrar_informacion()

if __name__ == "__main__":
  main()
