# FIND SONGS
#get songid and artistid from song and artist tables
song_select = ("""
     SELECT
         song.song_id,
         artist.artist_id
    FROM
        songs as song
    INNER JOIN
        artists as artist ON artist.artist_id = song.artist_id
    WHERE
        song.title = (%s) AND
        artist.name = (%s) AND
        song.duration = (%s);
""")