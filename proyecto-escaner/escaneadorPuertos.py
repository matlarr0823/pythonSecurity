import socket

# Pedir host (IP o nombre)
host = input("Introduce la IP o nombre del host (ej. 127.0.0.1): ")

# Pedir puerto inicial y validar que sea un número
while True:
    inicio_texto = input("Puerto inicial (ej. 20): ")
    if inicio_texto.isdigit():
        inicio = int(inicio_texto)
        break
    else:
        print("Por favor escribe solo números para el puerto inicial.")

# Pedir puerto final y validar que sea un número
while True:
    fin_texto = input("Puerto final (ej. 25): ")
    if fin_texto.isdigit():
        fin = int(fin_texto)
        break
    else:
        print("Por favor escribe solo números para el puerto final.")

# Asegurar que inicio no sea mayor que fin
if inicio > fin:
    print("El puerto inicial es mayor que el puerto final. Intercambiaré los valores.")
    temp = inicio
    inicio = fin
    fin = temp

# Pedir modo verboso (s/n)
verboso_texto = input("¿Modo verboso? (s/n): ").lower()
if verboso_texto == "s":
    verboso = True
else:
    verboso = False

print("Escaneando", host, "desde el puerto", inicio, "hasta", fin)

# Lista para guardar puertos abiertos
puertos_abiertos = []

# Bucle principal: probar puerto por puerto
for puerto in range(inicio, fin + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)  # esperar máximo 1 segundo por puerto
    resultado = s.connect_ex((host, puerto))
    if resultado == 0:
        # puerto abierto
        puertos_abiertos.append(puerto)
        if verboso:
            print("Puerto", puerto, "=> abierto")
    else:
        # puerto cerrado o no accesible
        if verboso:
            print("Puerto", puerto, "=> cerrado")
    s.close()

# Mostrar resumen final
if len(puertos_abiertos) == 0:
    print("No se encontraron puertos abiertos en ese rango.")
else:
    print("Puertos abiertos encontrados:")
    for p in puertos_abiertos:
        print("-", p)
