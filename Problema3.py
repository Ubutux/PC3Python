"""Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio"""

class CIRCULO:

  def __init__(self, radio):
    
    self.radio = radio

  def calcular_area(self):

    return 3.14159 * self.radio ** 2

def main():
  n=int(input("Ingrese el radio del circulo: "))
  circulo = CIRCULO (n)
  area = circulo.calcular_area()

  print(f"El área del círculo es: {area}")

if __name__ == "__main__":
  main()