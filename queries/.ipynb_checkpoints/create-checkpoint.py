# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id serial PRIMARY KEY,
        start_time timestamp REFERENCES time(start_time),
        user_id int REFERENCES users(user_id),
        level varchar(255) NOT NULL,
        song_id varchar(255) REFERENCES songs(song_id),
        artist_id varchar(255) REFERENCES artists(artist_id),
        session_id int NOT NULL,
        location text NOT NULL,
        user_agent text NOT NULL
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id int PRIMARY KEY,
        first_name varchar (255),
        last_name varchar (255),
        gender varchar(2),
        level varchar(255) NOT NULL
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id varchar(255) PRIMARY KEY,
        title varchar,
        artist_id varchar(255),
        year int NOT NULL,
        duration numeric NOT NULL
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR(255) PRIMARY KEY,
        name varchar(255) NOT NULL,
        location text NOT NULL,
        latitude numeric NOT NULL,
        longitude numeric NOT NULL
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time timestamp PRIMARY KEY,
        hour int NOT NULL,
        day int NOT NULL,
        week int NOT NULL,
        month int NOT NULL,
        year int NOT NULL,
        weekday int NOT NULL
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

