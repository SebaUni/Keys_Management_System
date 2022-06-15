from cryptography.fernet import Fernet

def ingresarUsuario():
    registroExistoso = 0
    while(registroExistoso != 1):
        username = input("Ingrese nombre de usuario:")
        contrasena_original = input("Ingrese su contraseña:")
        contrasena_confirmar = input("Confirme su contraseña: ")
        if(contrasena_confirmar == contrasena_original):
            registroExistoso = 1
            print("Ingreso exitoso")
        else:
            print("Las contraseñas no coinciden, intentelo nuevamente")
    return registroExistoso

def guardarEncriptado():
    key = Fernet.generate_key()
    f = Fernet(key)

    username = input("Ingrese nombre de usuario:")
    contrasena = input("Ingrese la contraseña:")
    aplicacion = input("Ingrese la aplicacion:")
    save = str.encode(username+contrasena+aplicacion)
    token = f.encrypt(save)

    with open("registros.txt", "a") as f1, open("key.txt", "a") as f2:
        f1.write(token)
        f2.write(key)

def verAplicaciones():
    username = input("Ingrese nombre de usuario:")
    contrasena = input("Ingrese la contraseña:")
    aplicaciones = []
    with open("registros.txt", "rb") as f1, open("key.txt", "rb") as f2:
        token = f1.read()
        key = f2.read()

    f = Fernet(key)
    text = str(f.decrypt(token),'utf-8') #converting back to string
    print(text)



def main():
    print("Bienvenido al sistema de registros, inicie sesión")
    ingresarUsuario()
    opcion = int(input("¿Que desea hacer? \n 1.Guardar Datos\n 2.Ver aplicaciones\n 3.Salir\n Ingrese su opción: "))
    while(True):
        if(opcion == 1):
            guardarEncriptado()
        elif(opcion == 2):
            verAplicaciones()
        elif(opcion == 3):
            break
        else:
            print("Opción invalida")
        opcion = int(input("¿Que desea hacer? \n 1.Guardar Datos\n 2.Ver aplicaciones\n 3.Salir\n Ingrese su opción: "))


main()


