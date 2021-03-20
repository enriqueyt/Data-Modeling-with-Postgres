import os
import glob
import psycopg2
import pandas as pd
from etl import main
from queries.create_tables import *

def init():
    cur, conn = createDB()
    main(cur, conn)
    conn.close()


if __name__ == "__main__":
    init()