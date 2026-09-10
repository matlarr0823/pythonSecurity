invitados=[]

nombre=input("Ingrese su nombre: ")

if nombre in invitados:  
        print("El invitado ya esta en la lista")
else:
    invitados.append(nombre)
    print("Invitado agregado a la lista")
    print("Lista de invitados:", invitados)

        