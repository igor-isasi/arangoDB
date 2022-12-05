from arango import ArangoClient

# Inicializar el cliente de ArangoDB
client = ArangoClient(hosts="http://mi-cluster-ip-arangodb:8529")

# Conexion a la base de datos _system como usuario root. La contraseña la hemos definido en el Dockerfile
sys_db = client.db(name='_system', username='root', password='root_passwd')

# Si la base de datos AS existe, borrarla y crearla de nuevo para que no haya documentos repetidos
if sys_db.has_database('AS'):
    sys_db.delete_database('AS')

sys_db.create_database('AS')

# Conexion a la base de datos AS como usuario root
db = client.db('AS', username='root', password='root_passwd')

# Crear una coleccion llamada profesores si no existe
if db.has_collection('profesores'):
    profesores = db.collection('profesores')
else:
    profesores = db.create_collection('profesores')

# Meter documentos en la coleccion profesores
profesores.insert({'nombre': 'Unai', 'apellido': 'Lopez'})

# Crear una coleccion llamada estudiantes si no existe
if db.has_collection('estudiantes'):
    estudiantes = db.collection('estudiantes')
else:
    estudiantes = db.create_collection('estudiantes')

# Meter documentos en la coleccion estudiantes
estudiantes.insert({'nombre': 'Igor', 'apellido': 'Isasi'})
estudiantes.insert({'nombre': 'Aitor', 'apellido': 'Sanchez'})
estudiantes.insert({'nombre': 'Pedro', 'apellido': 'Perez'})

# Ejecutar dos solicitudes AQL: una para la coleccion profesores y otra para la coleccion estudiantes
# Se devuelven cursores para poder recorrer los documentos
cursorProfesores = db.aql.execute('FOR doc IN profesores RETURN doc')
cursorEstudiantes = db.aql.execute('FOR doc IN estudiantes RETURN doc')


f = open("miVolumen/arangodb-AS.txt", "w")
# Iterar los cursores para conseguir la informacion de los documentos
f.write("___________________\n")
f.write("|    Profesores    |\n")
f.write("|__________________|\n")
for profesor in cursorProfesores:
    f.write(str(profesor['nombre']) + " " + str(profesor['apellido']) + "\n")
f.write("___________________\n")
f.write("|    Estudiantes   |\n")
f.write("|__________________|\n")

for estudiante in cursorEstudiantes:
    f.write(str(estudiante['nombre']) + " " + str(estudiante['apellido']) + "\n")
f.close()

while True:
    pass