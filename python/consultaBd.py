import sqlite3
conn = sqlite3.connect('estudiantes.db')
cursor = conn.cursor()

consulta = input("Nombre a Consultar: ")
print(consulta)
rows = cursor.execute(f"SELECT * FROM alumnos where nombre='{consulta}'")

data =rows.fetchone()

if data == None:
    print("Alumno no encontrado")
else:
    print(data)


cursor.close()
conn.close()