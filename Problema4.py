"""Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase."""

class RECTANGULO:

  def __init__(self, largo, ancho):

    self.largo = largo
    self.ancho = ancho

  def calcular_area(self):

    return self.largo * self.ancho

def main():

  b=int(input("Ingrese la base: "))
  a=int(input("Ingrese la altura: "))

  rectangulo = RECTANGULO(b, a)

  area = rectangulo.calcular_area()

  print(f"El área del rectángulo es: {area}")

if __name__ == "__main__":
  main()