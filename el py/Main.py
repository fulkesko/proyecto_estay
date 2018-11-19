from Funciones import *

while(True):
    print("----------------------")
    rut = input("ingrese rut: ").lower().strip()
    clave = input("ingrese clave: ").lower().strip()
    valid = ValidacionInicioSesion(rut, clave)
    if (valid == 1):
        print("inicio sesion correcto")
        menuPrincipal(rut)
        break
    elif (valid != 1):
        print("reingrese los datos!! ")
        print("----------------------")



