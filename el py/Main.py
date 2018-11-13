import mysql.connector
db = mysql.connector.connect(host='localhost',user='root',passwd='',database='blog2')
cursor = db.cursor()
