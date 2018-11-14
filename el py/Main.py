from Funciones import *

while(True):
    print("----------------------")
    nombre = input("ingrese nombre: ").lower().strip()
    clave = input("ingrese clave: ").lower().strip()
    valid = ValidacionInicioSesion(nombre, clave)
    if (valid == 1):
        break
    elif (valid != 1):
        print("reingrese los datos!! ")
        print("----------------------")
print("inicio sesion correcto")

