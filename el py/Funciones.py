import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',passwd='',database='hospital')
cursor = db.cursor()


def menuPrincipal(rut_empleado):
    print("-----Menú Principal-----")
    print("1.- Pacientes")
    print("2.- Consultas")
    opcion = input("->")
    if (opcion == '1'):
        print("1.- Ver pacientes")
        print("2.- Registrar pacientes")
        opc = input("->")
        if (opc == '1'):
            verPaciente()
        elif (opc == '2'):
            registrarPaciente()
    elif (opcion == '2'):
        print("1.- Ingresar Consulta")
        print("2.- Ver consultas")
        opc = input("->")
        if (opc == '1'):
            generar_consulta(rut_empleado)
        if (opc == '2'):
            pass

def verPaciente():
    sql="SELECT paciente.nombre,paciente.apellido,paciente.telefono,prevision.nombre " \
        "FROM paciente " \
        "INNER JOIN prevision ON paciente.prevision_id_fk = prevision.id"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print("|", "Nombre", "|", "Apellido", "|", "Telefono", "|", "Prevision")
    for fila in rs:

         print("|",(fila[0]),"|", fila[1],"|",fila[2],"|",fila[3],"|")

def ValidacionInicioSesion(rut, clave):
    sql = "SELECT count(*) FROM trabajador WHERE rut = '" +rut+ "' AND pass = SHA2('" +clave+ "',0)"
    cursor.execute(sql)
    rs = cursor.fetchall()
    valor = rs[0][0]
    return valor

def prevision():
    print("Seleccion de Prevision")
    print("1.-Fonasa")
    print("2.-Isapre")
    print("3.-No posee")
    print("----------------------")
    previ = input("->")

    return previ


def registrarPaciente():
    print("Registro de pacientes")
    print("")
    rut = input("rut: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Telefono: ")
    previ = prevision()

    sql = "INSERT INTO paciente VALUES(NULL, '"+rut+"', '"+nombre+"','"+apellido+"','"+telefono+"','"+previ+"')"
    cursor.execute(sql)
    db.commit()
    print ("->")

def existe_paciente(rut):
    sql = "SELECT COUNT(*) FROM paciente WHERE rut = '" + rut + " '"
    cursor.execute(sql)
    rs = cursor.fetchall()
    return rs[0][0] == 1

def generar_consulta(rut):
    paciente = input("Rut: ")
    if(existe_paciente(paciente)):
        observacion = input("observación: ")
        sql="INSERT INTO consulta VALUES (NULL,(SELECT id FROM paciente WHERE rut ='"+paciente+"'),(SELECT id FROM trabajador WHERE rut = '"+rut+"'),'"+observacion+"')"
        print(sql)
        cursor.execute(sql)
        db.commit()
    else:
        print("No existe paciente .. que desea hacer ? xd ")
        print("1.-Registrar")
        print("2.-Menu")
        op=input("->")
        if(op == '1'):
            registrarPaciente()
        else:
            menuPrincipal()

if __name__ == "__main__":
   verPaciente() #simulacion de login 121-1 de trabajador

