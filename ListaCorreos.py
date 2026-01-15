correos=[]

correo=input("Ingrese su correo electrónico: ")

if correo in correos:  
        print("El correo ya está en la lista")
else:
    correos.append(correo)
    print("Correo agregado a la lista")
    print("Lista de correos:", correos)