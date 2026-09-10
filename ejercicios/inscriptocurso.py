inscriptos=["Ana", "Luis", "Maria"]
lista_negra=["Pedro", "Jorge"]

usuario=input("Ingrese su nombre: ")

if usuario in inscriptos:
    print("El usuario ya está inscripto")
elif usuario in lista_negra:
    print("El usuario está en la lista negra, no puede inscribirse")
else:
    inscriptos.append(usuario)
    print("Usuario inscripto correctamente")
    print("Lista de inscriptos:", inscriptos)
