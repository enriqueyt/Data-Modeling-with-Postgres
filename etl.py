import os
import glob
import psycopg2
import pandas as pd
from queries import insert, select

def process_song_file(cur, conn, filepath):
    # open song file
    df = pd.read_json(filepath, lines = True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0].tolist()
    cur.execute(insert.song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0].tolist()
    cur.execute(insert.artist_table_insert, artist_data)


def process_log_file(cur, conn, filepath):
    # open log file
    df = pd.read_json(filepath, lines = True)

    # filter by NextSong action
    df = df[df["page"] == "NextSong"]

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = (
        t.tolist(),
        t.dt.hour.values.tolist(),
        t.dt.day.values.tolist(),
        t.dt.week.values.tolist(),
        t.dt.month.values.tolist(),
        t.dt.year.values.tolist(),
        t.dt.weekday.values.tolist()
    )
    column_labels = ('timestamp', 'hour', 'day', 'week of year', 'month', 'year', 'weekday')
    
    data = {}
    for i in range(len(column_labels)):
        data[column_labels[i]] = time_data[i]

    time_df = pd.DataFrame(data=data)

    for i, row in time_df.iterrows():
        cur.execute(insert.time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(insert.user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(select.song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (songid, t[index], row.userId, row.level, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(insert.songplay_table_insert, songplay_data)
        conn.commit()


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, conn, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main_etl(cur, conn):

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()
