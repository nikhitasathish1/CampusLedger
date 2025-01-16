import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Spotify01',
)

#preparing a cursor object
cursorObject = dataBase.cursor()

#creating a database
cursorObject.execute("CREATE DATABASE project_db")

print("All Done!")