import mysql.connector
db = mysql.connector.connect(host='localhost',user='root',passwd='',database='hospital')
cursor = db.cursor()

