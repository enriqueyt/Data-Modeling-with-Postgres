import os
import glob
import psycopg2
import pandas as pd
from etl import main
from queries.create_tables import *

def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    create_table.main()
    main(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()