import os
import glob
from etl import main_etl
from config.connection import getConnection
from queries.database import build_database

def init():
    cur, conn = getConnection()
    build_database(cur, conn)
    main_etl(cur, conn)

if __name__ == "__main__":
    init()