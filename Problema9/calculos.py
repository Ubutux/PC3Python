"""
Cree un módulo llamado operaciones.py el cual contendrá 4 funciones para realizar una suma,
una resta, un producto y una división entre dos números. Todas ellas devolverán el resultado.
En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para
evitar que se quede bloqueada una funcionalidad, esto incluye:
● En caso de que se envíen valores a las funciones que no sean números, deberá
aparecer un mensaje que informe Error: Tipo de dato no válido.
● En caso de realizar una división por cero, deberá aparecer un mensaje que informe
Error: No es posible dividir entre cero.
Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás
importar el módulo y ejecutar las funciones.
"""

import operaciones

if __name__ == "__main__":
    num1 = 10
    num2 = 0

    print("Suma:", operaciones.suma(num1, num2))
    print("Resta:", operaciones.resta(num1, num2))
    print("Producto:", operaciones.producto(num1, num2))
    print("División:", operaciones.division(num1, num2))
