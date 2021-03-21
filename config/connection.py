import psycopg2

def getConnection():
    """
    Open a connection to Postgres db 

    Returns:
        conn: the current connection
        cur: the cursor from conection
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    return cur, conn
