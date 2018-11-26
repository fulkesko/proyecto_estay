import mysql.connector
from ValidadorVacios import *

db = mysql.connector.connect(host='localhost',user='root',passwd='',database='hospital')
cursor = db.cursor()



def menuPrincipal(rut_empleado):
    while(True):
        print("")
        print("-----Menú Principal-----")
        print("Ingrese una opción")
        print("1.- Pacientes")
        print("2.- Consultas")
        print("3.- Salir")
        opcion = s_input("->")
        if (opcion == '1'):
            print("-----Pacientes-----")
            print("1.- Ver pacientes")
            print("2.- Registrar pacientes")
            print("3.- Volver atras")
            opc = s_input("->")
            if (opc == '1'):
                verPaciente()
            elif (opc == '2'):
                registrarPaciente()
            elif (opc == '3'):
                menuPrincipal(rut_empleado)
        elif (opcion == '2'):
            print("-----Consultas-----")
            print("1.- Ingresar Consulta")
            print("2.- Ver Consultas")
            print("3.- Volver atras")
            opc = s_input("->")
            if (opc == '1'):
                generar_consulta(rut_empleado)
            elif (opc == '2'):
                verConsulta()
            elif(opc == '3'):
                menuPrincipal(rut_empleado)

        elif(opcion == '3'):
            print("-----salida exitosa-----")
            break
        else:
            print("ingrese una opción valida!!")

def verConsulta():
    sql ="SELECT paciente.nombre,trabajador.nombre,consulta.fecha, consulta.observacion FROM consulta " \
         "INNER JOIN paciente ON consulta.paciente_id_fk = paciente.id " \
         "INNER JOIN trabajador ON consulta.trabajador_id_fk  = trabajador.id "
    cursor.execute(sql)
    rs = cursor.fetchall()
    print("|", "Paciente", "|", "Trabajador", "|", "Fecha","|"," Observacion","|")
    for fila in rs:
        print("|", (fila[0]), "|", fila[1], "|", fila[2], "|",fila[3])


def verPaciente():
    sql="SELECT paciente.nombre,paciente.apellido,paciente.telefono,prevision.nombre " \
        "FROM paciente " \
        "INNER JOIN prevision ON paciente.prevision_id_fk = prevision.id"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print("|", "Nombre", "|", "Apellido", "|", "Telefono", "|", "Prevision","|")
    for fila in rs:

         print("|",(fila[0])," | ", fila[1],"|",fila[2],"|",fila[3],"|")

def ValidacionInicioSesion(rut, clave):
    sql = "SELECT count(*) FROM trabajador WHERE rut = '" +rut+ "' AND pass = SHA2('" +clave+ "',0)"
    cursor.execute(sql)
    rs = cursor.fetchall()
    valor = rs[0][0]
    return valor

def prevision():
    print("-----Seleccion de Prevision-----")
    print("1.-Fonasa")
    print("2.-Isapre")
    print("3.-No posee")
    print("--------------------------------")
    previ = s_input("->")

    return previ


def registrarPaciente():
    print("-----Registro de pacientes-----")
    print("")
    rut = s_input("Rut: ")
    nombre = s_input("Nombre: ")
    apellido = s_input("Apellido: ")
    telefono = s_input("Telefono: ")
    previ = prevision()

    sql = "INSERT INTO paciente VALUES(NULL, '"+rut+"', '"+nombre+"','"+apellido+"','"+telefono+"','"+previ+"')"
    cursor.execute(sql)
    db.commit()
    print ("-----Registro exitoso-----")
    print ("")

def existe_paciente(rut):
    sql = "SELECT COUNT(*) FROM paciente WHERE rut = '" + rut + " '"
    cursor.execute(sql)
    rs = cursor.fetchall()
    return rs[0][0] == 1

def generar_consulta(rut):
    paciente = s_input("Rut Paciente: ")
    if(existe_paciente(paciente)):
        observacion = s_input("observación: ")
        sql="INSERT INTO consulta VALUES (NULL,(SELECT id FROM paciente WHERE rut ='"+paciente+"'),(SELECT id FROM trabajador WHERE rut = '"+rut+"'),'"+observacion+"')"
        print(sql)
        cursor.execute(sql)
        db.commit()
    else:
        print("No existe paciente .. que desea hacer ?")
        print("1.-Registrar")
        print("2.-Menu Principal")
        op = s_input("->")
        if(op == '1'):
            registrarPaciente()
        elif(op == '2'):
            menuPrincipal()

if __name__ == "__main__":
   verConsulta() #simulacion de login 121-1 de trabajador

