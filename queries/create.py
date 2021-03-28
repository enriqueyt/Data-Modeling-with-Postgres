# CREATE TABLES

songplay_table_create = ("""
     CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL UNIQUE PRIMARY KEY,
        start_time timestamp NOT NULL,
        user_id int NOT NULL,
        level varchar(255),
        song_id varchar(255),
        artist_id varchar(255),
        session_id int,
        location text,
        user_agent text
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id int PRIMARY KEY,
        first_name varchar(255),
        last_name varchar(255),
        gender varchar(2),
        level varchar(255)
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id varchar(255) PRIMARY KEY,
        title varchar,
        artist_id varchar(255),
        year int,
        duration numeric
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR(255) PRIMARY KEY,
        name varchar(255),
        location text,
        latitude numeric,
        longitude numeric
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time timestamp PRIMARY KEY,
        hour int,
        day int,
        week int,
        month int,
        year int,
        weekday int
    );
""")

# QUERY LISTS

create_table_queries = [
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
    songplay_table_create
]

