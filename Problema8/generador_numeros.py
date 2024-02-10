import random

def generar_numeros():
    numeros = [random.randint(0, 100) for _ in range(20)]
    return numeros

def mostrar_lista(lista):
    print("Lista de números generados:")
    print(lista)

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)