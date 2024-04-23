import csv
import psycopg2

#Función para crear la base de datos
def create_database():
    conn = psycopg2.connect(
                            host='ep-lively-scene-a5ep6js6.us-east-2.aws.neon.tech',
                            database='neondb',
                            user='neondb_owner',
                            password='2nPY0bGaHwur')
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE DATABASE basedatoslab1")
    cur.close()
    conn.close()

#create_database()

#Función para crear la tabla con los datos del dataset
def add_dataset():
    conn = psycopg2.connect(
                            host='ep-lively-scene-a5ep6js6.us-east-2.aws.neon.tech',
                            database='neondb',
                            user='neondb_owner',
                            password='2nPY0bGaHwur')
    conn.autocommit = True
    cur = conn.cursor()

    # Crear la nueva tabla para los cursos online
    crear_tabla = """CREATE TABLE Courses_Clean_tabla (
        id INT,
        course_id VARCHAR(255),
        userid_DI VARCHAR(255),
        registered INT,
        viewed INT,
        explored INT,
        certified INT,
        final_cc_cname_DI VARCHAR(255),
        LoE_DI VARCHAR(255),
        YoB INT,
        gender VARCHAR(5),
        grade FLOAT,
        start_time_DI DATE,
        last_event_DI DATE,
        nevents INT,
        ndays_act INT,
        nplay_video INT,
        nchapters INT,
        nforum_posts INT,
        incomplete_flag INT
    )"""
    
    cur.execute(crear_tabla)
    
    # Insertar datos desde el archivo CSV
    with open('Dataset/CourClean.csv', 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        next(lector)  # Saltar la cabecera
        
        for fila in lector:
            fila = [None if x == '' or x.isspace() else x for x in fila]
            cur.execute("INSERT INTO Courses_Clean_tabla (id, course_id, userid_DI, registered, viewed, explored, certified, final_cc_cname_DI, LoE_DI, YoB, gender, grade, start_time_DI, last_event_DI, nevents, ndays_act, nplay_video, nchapters, nforum_posts, incomplete_flag) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                fila
            )
    print('Programa ejecutado correctamente')
    cur.close()
    conn.close()

#add_dataset()

#Función para eliminar la tabla si existe
def eliminar_tabla():
    conn = psycopg2.connect(
                            host='ep-lively-scene-a5ep6js6.us-east-2.aws.neon.tech',
                            database='neondb',
                            user='neondb_owner',
                            password='2nPY0bGaHwur')
    conn.autocommit = True
    cur = conn.cursor()

    # Eliminar la tabla si existe
    eliminar_tabla = "DROP TABLE IF EXISTS Courses_Clean_tabla"
    cur.execute(eliminar_tabla)

    cur.close()
    conn.close()


#eliminar_tabla()