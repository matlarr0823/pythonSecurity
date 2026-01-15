productos=["mouse", "teclado", "monitor"]

nombre=input("Ingrese el producto a comprar: ")

if nombre in productos:
    print("Producto Disponible")
else:
    print("Producto No Disponible")