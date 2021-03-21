from .create import create_table_queries
from .drop import drop_table_queries

def build_database(cur, conn):
    """
    Build the database structure. it call function to drop and create tables

    Args:
        cur: Current cursor current from coonnection open.
        conn: Current connection.

    Returns:
        void
    """

    drop_tables(cur, conn)
    create_tables(cur, conn)


def drop_tables(cur, conn):
    """
    Iterate drop queries and execute them

    Args:
        cur: Current cursor current from coonnection open.
        conn: Current connection.

    Returns:
        void
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Iterate create queries and execute them

    Args:
        cur: Current cursor current from coonnection open.
        conn: Current connection.

    Returns:
        void
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
