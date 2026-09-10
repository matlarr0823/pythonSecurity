Lista = input("Ingrese una lista de números separados por comas: ")

def sumar_lista(entrada):
    numeros = [int(num) for num in entrada.split(',')]
    suma = sum(numeros)
    return suma
    
print("La suma de los números en la lista es:", sumar_lista(Lista))