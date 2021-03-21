import os
import glob
from etl import main_etl
from config.connection import getConnection
from queries.database import build_database

def init():
    """
    Starting point to run the ELT. 
        step will do:
            - It will get a new connection
            - build database structure
            - call main function to start the process of ETL

    Returns:
        void
    """
    cur, conn = getConnection()
    build_database(cur, conn)
    main_etl(cur, conn)

if __name__ == "__main__":
    init()