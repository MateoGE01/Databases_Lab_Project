#Se creará la base de datos en PostgreSQL con Python, luego se añadirá el dataset a la base de datos
import psycopg2
from psycopg2 import sql

# Conectarse a PostgreSQL con el usuario postgres (o un usuario con los permisos necesarios)
conn = psycopg2.connect(
    host="your_host",
    user="postgres",
    password="your_password"
)

# Crear un nuevo cursor
cur = conn.cursor()

# Crear una nueva base de datos
cur.execute(
    sql.SQL(
        "CREATE DATABASE {}"
    ).format(sql.Identifier('your_database'))
)

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cur.close()
conn.close()

"""
Entiendo, estás utilizando Koyeb, un servicio de contenedores en la nube. Sin embargo, el proceso para crear una base de datos PostgreSQL utilizando Python no cambia.

Primero, necesitas asegurarte de tener un servicio PostgreSQL en ejecución en Koyeb. Luego, puedes usar el código que te proporcioné anteriormente para crear una nueva base de datos.

El host será la dirección IP o el nombre del dominio del servicio PostgreSQL en Koyeb, y el usuario y la contraseña serán los que hayas configurado para el servicio PostgreSQL.

Si tienes problemas para encontrar estos detalles, te recomendaría que consultes la documentación de Koyeb o te pongas en contacto con su soporte técnico.
"""