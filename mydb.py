import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1144",

)

# Prepare a cursor object using cursor() method
cursor = database.cursor()

# Create a database in MySQL server
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE dcrmco")

print("Database is created successfully")