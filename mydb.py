import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Anil@2002'
)


# prepare a cursor object

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE anilscrm")

print('All Done!')

