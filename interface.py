import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",passwd="",database="hospitals")
mycursor=mydb.cursor()
mycursor.execute("select*from hospital")
for table in mycursor:
    print(table) 