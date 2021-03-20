# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS users CASCADE;"
user_table_drop     = "DROP table IF EXISTS songs CASCADE;"
song_table_drop     = "DROP table IF EXISTS artists CASCADE;"
artist_table_drop   = "DROP table IF EXISTS time CASCADE;"
time_table_drop     = "DROP table IF EXISTS songplays CASCADE;"


drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]