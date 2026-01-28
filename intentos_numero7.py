intentos = 0
numero = 0

while numero != 7:
    numero = int(input("Escribe un número: "))
    intentos += 1
    
    if numero != 7:
        print(f"No es correcto, intenta de nuevo.")

print(f"\n¡Correcto! Escribiste 7 en el intento número {intentos}")
