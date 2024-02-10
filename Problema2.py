"""Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)"""

def obtener_calificaciones():

  calificaciones_str = input("Ingrese una lista de calificaciones separadas por comas: ")

  calificaciones_str = calificaciones_str.split(",")

  calificaciones_int = []
  for calificacion_str in calificaciones_str:
    try:
      calificacion_int = int(calificacion_str)
      calificaciones_int.append(calificacion_int)
    except ValueError:
      print(f"Error: La calificación '{calificacion_str}' no es un número válido.")

  return calificaciones_int

def main():

  calificaciones = obtener_calificaciones()

  print(f"Las calificaciones son: {calificaciones}")

if __name__ == "__main__":
  main()