import mysql.connector

connection = mysql.connector.connect(
    user='root', password='root', host='mysql',port='3306', database='db'
)

print("Banco de dados conectado!")

cursor = connection.cursor()
cursor.execute('Select * FROM estudantes')
estudantes = cursor.fetchall()
connection.close()

print(estudantes)