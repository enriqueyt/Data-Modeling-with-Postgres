import psycopg2

def getConnection():

    cur, conn = getConn()

    #cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    #cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    conn.close()

    return getConn()

def getConn():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    return cur, conn