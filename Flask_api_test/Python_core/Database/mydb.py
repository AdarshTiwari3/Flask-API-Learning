import mysql.connector

myDatabase = mysql.connector.connect(host="localhost", user="root", password="admin")

myCursor = myDatabase.cursor() #this is used to interact with the database, it will execute the queries and store the result in it

myCursor.execute("CREATE DATABASE mydb") #this will create a database with the name mydb

myCursor.execute("SHOW DATABASES") #this will show all the databases present in the database server, lower case also works

for db in myCursor:
    print("My Databases are:",db)
