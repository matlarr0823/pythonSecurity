usuariospermitidos=["Let", "LetAdmin", "AndAdmin"]

usuariosblockeados=["Hacker1", "MalwarePro", "SpyUser"]

usuario=input("Ingrese su nombre de usuario: ")

if usuario in usuariospermitidos:
    print("Acceso Permitido")
elif usuario in usuariosblockeados: 
    print("Acceso Denegado")
else:
    print("Usuario Desconocido")
