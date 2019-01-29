import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",passwd="",database="library")

mycursor = mydb.cursor()

mycursor.execute("select * from book")

result = mycursor.fetchall()

for i in result:
	print(i)