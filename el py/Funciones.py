import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',passwd='',database='hospital')
cursor = db.cursor()

def MenuPrincipal():

    pass

def ValidacionInicioSesion(rut, clave):
    sql = "SELECT count(*) FROM trabajador WHERE rut = '" +rut+ "' AND pass = SHA2('" +clave+ "',0)"
    cursor.execute(sql)
    rs = cursor.fetchall()
    valor = rs[0][0]
    return valor

def prevision( ):
    print("Seleccion de Prevision")
    print("1.-Fonasa")
    print("2.-Isapre")
    print("3.-No posee")
    print("----------------------")
    previ = input("Ingrese Opción: ")

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
    print ("ingreso correcto")

def generar_consulta(rut):
    paciente = input("Nombre: ")
    observacion = input("observación: ")

