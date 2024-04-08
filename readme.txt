This is a python framework used to easily connect to a postgres database using the psycopg2 package for analysis in jupyter notebook or automated sql runs. 
Automated runs of sql (table creation, inserts, etc.) can be performed by populating the sql directory 1 or more .sql files and runnung the run_sql_queries_in_directory function.

How to run:
* populate the postgresql section of the database.ini file with actual database credentials
* the get_db_connection function in config.py will parse the .ini file (.ini file name should be an input to the function)
* see the run_sql_queries_in_directory function in functions.py as an example
