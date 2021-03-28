# Data Modeling with Postgres


## Getting Started


## Summary

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app



## Schema

#### **Fact Table**
* songplays - records in log data associated with song plays i.e. records with page NextSong
    songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent


#### **Dimension Tables**
* users - users in the app
    ( user_id, first_name, last_name, gender, level )
* songs - songs in music database
    ( song_id, title, artist_id, year, duration )
* artists - artists in music database
    ( artist_id, name, location, latitude, longitude )
* time - timestamps of records in songplays broken down into specific units
    () start_time, hour, day, week, month, year, weekday )



## Prerequisites/Installing

In order to run the project have to be intalled following programs

### Git

Go to the [oficial page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and choose your OS


### Python

* macOS and OS X

```
$ xcode-select --install
```

or through brew

```
$ brew install openssl xz gdbm
```


* Linux

```
$ sudo apt-get update
$ sudo apt-get build-dep python3.6
```

### psycopg2

```
$ pip install psycopg2
```

### Pandas

```
$ pip install pandas
```


### Docker

In order to run Postgres and not install it in your machine we can do iit throuhgt Postgres (Just if you done have it intalled)


```
$  sudo apt-get update
$  sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Or go to this [link](https://docs.docker.com/engine/install/) for the official webside and choose your OS


## Project Structure

    .
    ├── config                  # configutation file for connections
        └── connection.py       # create a connection and retrieve the conncecttion and the cursor
    ├── data                    # file that contain the data to store in our database
        ├── log_data            # Loag data by year
           └── 2018             # year of the data
                └── 11          # refering to the month
                    └── *.json  # Json files per day
    │   └── songdata            # End-to-end, integration tests (alternatively `e2e`)
            ├── A               
                ├── A            
                    ├──          # Json file that contains metadata about a song and the artist of that song
                ├── B 
                    ├──          # Json file that contains metadata about a song and the artist of that song          
                └── C  
                    ├──          # Json file that contains metadata about a song and the artist of that song          
            └── B            
                ├── A      
                    ├──          # Json file that contains metadata about a song and the artist of that song      
                ├── B     
                    ├──          # Json file that contains metadata about a song and the artist of that song       
                └── C        
                    ├──          # Json file that contains metadata about a song and the artist of that song   
    ├── queries                 # Contains querys or the the project
        ├── create_db           # create the database to worrk on
        ├── database            # run drop and create tables
        ├── drop                # contains querys to drop tables
        ├── create              # contains querys to create tables
        ├── insert              # contains querys to drop tables
        └── select              # contains select querys           
    ├── etl.py                  # reads and processes files from song_data and log_data and loads them into tables
    ├── etl.py                  # start point of the process
    ├── docker-compose.yml      # create a postgres image
    └── README.md


## Steps to Usage

1. Clone the repository

    ```
    $ git clone https://github.com/enriqueyt/Data-Modeling-with-Postgres.git
    ```

2. Up postgres

    If you dont have postgres in you local machine then run docker

    ```
    $ docker-compose up -d

    ```

3. Run the process

    A. Create the DB 
        
        ```
        $ python queries/create_db.py
        ```
    
    B. Run the ETL

        ```
        $ python init.py
        ```



## Authors

* **Enrique Yepez** - *Prject Data Modeling witth Postgres* - [Data-Modeling-with-Postgres](https://github.com/enriqueyt/Data-Modeling-with-Postgres)

