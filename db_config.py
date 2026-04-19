import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="database@2026",
        database="student_manager"
    )

    return conn

if get_connection():
    print("Connected successfully")