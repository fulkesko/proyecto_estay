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
            MenuPrincipal()

if __name__ == "__main__":
    generar_consulta('121-1') #simulacion de login 121-1 de trabajador

