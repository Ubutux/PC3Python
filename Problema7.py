"""
Modulo3/Ejercicios/Ejercicio2
Implementación clase Punto según las indicaciones del ejercicio
"""

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen"
        elif self.x == 0:
            return "El punto está sobre el eje Y"
        elif self.y == 0:
            return "El punto está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "El punto está en el cuadrante 1"
        elif self.x < 0 and self.y > 0:
            return "El punto está en el cuadrante 2"
        elif self.x < 0 and self.y < 0:
            return "El punto está en el cuadrante 3"
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuadrante 4"

    def vector(self, otro_punto):
        vector_x = otro_punto.x - self.x
        vector_y = otro_punto.y - self.y
        return Punto(vector_x, vector_y)

    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        return distancia


class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()

if __name__ == "__main__":
    punto1 = Punto(2, 3)
    punto2 = Punto(5, 7)

    print("Punto 1:", punto1)
    print("Punto 2:", punto2)

    print("Cuadrante de Punto 1:", punto1.cuadrante())
    print("Cuadrante de Punto 2:", punto2.cuadrante())

    print("Vector entre Punto 1 y Punto 2:", punto1.vector(punto2))

    print("Distancia entre Punto 1 y Punto 2:", punto1.distancia(punto2))

    rectangulo = Rectangulo(punto1, punto2)
    print("Base del rectángulo:", rectangulo.base())
    print("Altura del rectángulo:", rectangulo.altura())
    print("Área del rectángulo:", rectangulo.area())