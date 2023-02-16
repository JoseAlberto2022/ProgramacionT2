
import sqlite3 as lite
import sys


conexion = lite.connect("apellidos.sqlite")


cursor = conexion.cursor()


cursor.execute("SELECT * FROM APELLIDOS;")


datos = cursor.fetchall()

for i in datos:
    print("apellidos:",i[1],"\t numero:",i[2])

    print("identificador:",i[0]) 
