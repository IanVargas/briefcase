
"""
1. Cree un programa que le pida tres números al usuario y muestre el resultado de su suma.


"""


def sumar_numeros(suma):
    i=0
    while i < 3:
        numero = int(input("digite un numero"))
        suma = numero + suma
        i = i+1 
        
    return suma

valor = sumar_numeros(0)

print(valor)