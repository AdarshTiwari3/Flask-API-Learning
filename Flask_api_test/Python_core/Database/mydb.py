import mysql.connector

myDatabase = mysql.connector.connect(host="localhost", user="root", password="admin", database="mydb")

myCursor = myDatabase.cursor() #this is used to interact with the database, it will execute the queries and store the result in it

myCursor.execute("select * from student") #this will create a database with the name mydb
 
results = myCursor.fetchall() #this will fetch all the records from the table student

for i in myCursor:
    print(i)

#both are same
for i in results:
    print(i)
