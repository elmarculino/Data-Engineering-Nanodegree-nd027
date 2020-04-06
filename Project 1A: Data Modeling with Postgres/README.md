# Project: Data Modeling with Postgres

## Song Play Analysis

### Project goals

- Create a star schema with fact and dimension tables optimized for queries. 
- Build an ETL pipeline to transfer data from JSON log files to Postgres tables.

### Database purpose

It's not easy to analyse and extract valuable insights from log files. The first step to make this data useful is develop an ETL pipeline to load the log files data to an database. In a database is a lot easier to run queries and analyse the data. 

### Database schema

It was developed a star schema with the fact table _songplays_ and the dimension tables _users, songs, artists, time_ so the analytics team can run simpler queries with faster aggregations.

#### Fact Table
- __songplays__ - records in log data associated with song plays i.e. records with page NextSong
-- songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

#### Dimension Tables
- __users__ - users in the app
-- user_id, first_name, last_name, gender, level
- __songs__ - songs in music database
-- song_id, title, artist_id, year, duration
- __artists__ - artists in music database
-- artist_id, name, location, latitude, longitude
- __time__ - timestamps of records in songplays broken down into specific units
-- start_time, hour, day, week, month, year, weekday

### ETL pipeline

To execute the ETL process the log files are imported to a pandas dataframes where the necessary transformations are applied and the data is inserted in the database tables following the steps below: 

- Process song data files
	1.  Extract Data for Songs Dimension Table 
	2.  Extract Data for Artists Dimension Table
-  Process log data files
	3.  Extract Data for Time Dimension Table
	4.  Extract Data for Users Dimension Table
	5.  Extract Data and Songplays Fact Table

### Project Files

The project includes six files:

1.  `test.ipynb`  displays the first few rows of each table to let you check your database.
2.  `create_tables.py`  drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
3.  `etl.ipynb`  reads and processes a single file from  `song_data`  and  `log_data`  and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4.  `etl.py`  reads and processes files from  `song_data`  and  `log_data`  and loads them into your tables. You can fill this out based on your work in the ETL notebook.
5.  `sql_queries.py`  contains all your sql queries, and is imported into the last three files above.
6.  `README.md`  provides discussion on your project.

###  How to Run

Below are steps you can follow to complete the project:

1. Run  `create_tables.py`  to create your database and tables.
2. Run  `etl.py`  to load the data from the log files to the database.
3. Run  `test.ipynb`  to confirm the creation of your tables with the correct columns and to confirm that records were successfully inserted into each table. 