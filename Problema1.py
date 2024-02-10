"""
Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser menor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
cualquier excepción como ValueError o ZeroDivisionError.
Ejemplos:
- Input: 4/0 Acción: Volver a preguntar al usuario dada la excepción ZeroDivisionError
- Input 1.5/3 Acción: Error dado que solo se permiten números enteros ValueError
- Input 5/4 Acción: Volver a preguntar al usuario
- Input 3/4 Output: 75%
- Input 4/4: Output F
"""

def obtener_fraccion():

  while True:
    try:
      fraccion_str = input("Ingrese la fracción (X/Y): ")

      numerador, denominador = map(int, fraccion_str.split("/"))

      if not isinstance(numerador, int) or not isinstance(denominador, int):
        raise ValueError("Los valores deben ser números enteros")

      if denominador == 0:
        raise ZeroDivisionError("El denominador no puede ser 0")

      if numerador > denominador:
        raise ValueError("El numerador no puede ser mayor que el denominador")

      return numerador, denominador
    except ValueError as e:
      print(f"Error: {e}")
    except ZeroDivisionError as e:
      print(f"Error: {e}")

def calcular_porcentaje(numerador, denominador):

  porcentaje = round((numerador / denominador) * 100, 0)

  if porcentaje < 1:
    return "E"
  elif porcentaje > 99:
    return "F"
  else:
    return f"{porcentaje}%"

def main():

  numerador, denominador = obtener_fraccion()

  porcentaje = calcular_porcentaje(numerador, denominador)

  print(f"El porcentaje de combustible es: {porcentaje}")

if __name__ == "__main__":
  main()