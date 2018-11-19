import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',passwd='',database='hospital')
cursor = db.cursor()

def MenuPrincipal():

    pass

def ValidacionInicioSesion(nombre, clave):
    sql = "SELECT COUNT(*) FROM trabajador WHERE nombre = '" +nombre+ "' AND pass = SHA2('" +clave+ "',0)"
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
    previ=input("Ingrese Opción: ")

    return previ


def Consulta():
    pass
