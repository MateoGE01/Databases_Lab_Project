import csv
import psycopg2

def create_database():
    conn = psycopg2.connect(host='localhost', 
                            dbname='testdb', 
                            user='postgres', 
                            password='Test1234')
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE DATABASE basedatoslab1")
    cur.close()
    conn.close()

#create_database()


def add_dataset():
    conn = psycopg2.connect(host='localhost', 
                            dbname='basedatoslab1', 
                            user='postgres', 
                            password='Test1234')
    conn.autocommit = True
    cur = conn.cursor()


    #Primero se DEBE BORRAR LA TABLA Y CAMBIAR POR OTRA(se cambiará este mensaje cuando el dataset ya no sea de colombianos sino otro)
    crear_tabla = """CREATE TABLE colombianos_detenidos_exterior_tabla (
        FECHA_PUBLICACION DATE,
        PAIS_PRISION VARCHAR(255),
        CONSULADO VARCHAR(255),
        DELITO VARCHAR(255),
        EXTRADITADO_Y_O_REPATRIADO VARCHAR(255),
        SITUACION_JURIDICA VARCHAR(255),
        GENERO VARCHAR(255),
        GRUPO_EDAD VARCHAR(255),
        UBICACION_PAIS VARCHAR(255),
        CANTIDAD INT,
        LATITUD FLOAT,
        LONGITUD FLOAT
    )"""

    cur.execute(crear_tabla)
    #SE DEBE CAMBIAR POR OTRO DATASET
    with open('Dataset/colombianos_detenidos_exterior_Clean.csv', 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        next(lector)

        for fila in lector:
            cur.execute("INSERT INTO colombianos_detenidos_exterior_tabla (FECHA_PUBLICACION, PAIS_PRISION, CONSULADO, DELITO, EXTRADITADO_Y_O_REPATRIADO, SITUACION_JURIDICA, GENERO, GRUPO_EDAD, UBICACION_PAIS, CANTIDAD, LATITUD, LONGITUD) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        , fila
                        )
    cur.close()
    conn.close()

#add_dataset()


