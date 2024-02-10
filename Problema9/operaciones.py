
def suma(num1, num2):
    try:
        resultado = num1 + num2
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def resta(num1, num2):
    try:
        resultado = num1 - num2
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def producto(num1, num2):
    try:
        resultado = num1 * num2
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def division(num1, num2):
    try:
        if num2 == 0:
            raise ZeroDivisionError
        resultado = num1 / num2
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero"