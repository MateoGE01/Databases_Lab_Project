import psycopg2

def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_eSci7EKUL5XI0HTq6FC@pg-9b1eec3-uninorte.h.aivencloud.com:21563/basedatoslab1?sslmode=require')

    query_sql = 'SELECT course_id FROM Courses_Clean_tabla LIMIT 10'

    cur = conn.cursor()
    cur.execute(query_sql)

    rows = cur.fetchall()
    for row in rows:
        print(row[0])

    conn.close()


if __name__ == "__main__":
    main()
