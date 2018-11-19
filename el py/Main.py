from Funciones import *

while(True):
    print("----------------------")
    rut = input("ingrese rut: ").lower().strip()
    clave = input("ingrese clave: ").lower().strip()
    valid = ValidacionInicioSesion(rut, clave)
    if (valid == 1):
        generar_consulta(rut)
        break
    elif (valid != 1):
        print("reingrese los datos!! ")
        print("----------------------")
print("inicio sesion correcto")
menuPrincipal()


