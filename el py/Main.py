from Funciones import *

while(True):
    nombre = input("ingrese nombre: ").lower().strip()
    clave = input("ingrese clave: ").lower().strip()
    valid = ValidacionInicioSesion(nombre, clave)
    if (valid == 1):
        break
print("inicio sesion correcto")

