from Funciones import *
from ValidadorVacios import *

while(True):
    print("----------------------")
    rut = s_input("rut: ").lower().strip()
    clave = s_input("clave: ").lower().strip()
    valid = ValidacionInicioSesion(rut, clave)
    if (valid == 1):
        print("inicio sesion correcto !")
        menuPrincipal(rut)
        break
    elif (valid != 1):
        print("reingrese los datos!! ")
        print("----------------------")



