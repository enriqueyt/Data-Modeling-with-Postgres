# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS users"
user_table_drop     = "DROP table IF EXISTS songs"
song_table_drop     = "DROP table IF EXISTS artists"
artist_table_drop   = "DROP table IF EXISTS time"
time_table_drop     = "DROP table IF EXISTS songplays"


drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop
]