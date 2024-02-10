"""Cree un menú que reutilice a manera de módulos las clases creadas en los ejercicios 3 y 4. El
menú para utilizar deberá tener las siguientes funcionalidades:
1. Calcular el área de un circulo
2. Calcular el área de un rectangulo
3. Calcular el área de un cuadrado
4. Salir.
"""

from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    area = circulo.calcular_area()
    print(f"El área del círculo es: {area:.2f}")

def calcular_area_rectangulo():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo = Rectangulo(largo, ancho)
    area = rectangulo.calcular_area()
    print(f"El área del rectángulo es: {area:.2f}")

def calcular_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    cuadrado = Cuadrado(lado)
    area = cuadrado.calcular_area()
    print(f"El área del cuadrado es: {area:.2f}")

def main():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calcular_area_circulo()
        elif opcion == "2":
            calcular_area_rectangulo()
        elif opcion == "3":
            calcular_area_cuadrado()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()