temperaturas=["0", "15", "25", "30", "40"]

grado=input("Ingrese la temperatura: ")

if grado < 15:
    print("hace frio")
elif grado >= 15 and grado <= 25:
    print("Clima agradable")
else:
    print("Hace calor")