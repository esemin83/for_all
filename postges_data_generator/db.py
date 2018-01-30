import psycopg2

conn = psycopg2.connect(dbname="db", user="postgres", password="")


def select():
    try:
        list = []
        cur = conn.cursor()
        cur.execute("SELECT * FROM clients")
        for row in cur:
            list.append(row)
    except psycopg2.Error as e:
        print(e)
    finally:
        cur.close()
    return list


def insert_into_clients(client_id, address, through_id):
    try:
        cur = conn.cursor()
        cur.execute("SELECT insert_to_clients('%s', '%s', '%s'); COMMIT;" % (client_id, address, through_id))
    except Exception as e:
        print(e)
    finally:
        cur.close()
