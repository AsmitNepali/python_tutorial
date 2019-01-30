import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="", 
    database="library")

mycrousor = mydb.cursor()

# Field name
bookname = input("Enter Bookname: ")
author = input("Enter Author Name: ")
classs = input("Enter your class: ")
total = input("Enter total no. of books: ")
pprice = input("Enter unit price of book: ")
publication = input("Enter publication of book: ")

query = "INSERT INTO book (bookname, author, total, class, price, publication) VALUES(%s,%s,%s,%s,%s,%s)"
val = (bookname, author,int(total),int(classs),int(pprice),publication)

mycrousor.execute(query,val)

mydb.commit()

print(mycrousor.rowcount, "record added")

# mycrousor.execute("")