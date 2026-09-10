objectos=["espada", "llave", "pocion"]

objeto=input("Ingrese el objeto que desea recoger: ")

if objeto == "llave":
    print("Podes abrir la puerta")
elif objeto in objectos and objeto != "llave":
    print("Tenes el objeto pero no te sirve para abrir la puerta")
else:
    print("No tenes ese objeto")