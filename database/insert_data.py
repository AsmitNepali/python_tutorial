import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="library")
mycrousor = mydb.cursor()

query = "INSERT INTO book (bookname, author, total,) VALUES(%s,%s,%d)"
val = ("Fundamental IT", "Ram Krishna Aryal", 12)

mycrousor.execute(query,val)

mydb.commit()

print(mycrousor.rowcount, "record added")

# mycrousor.execute("")