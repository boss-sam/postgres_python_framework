from config import *
import time
import datetime
import os
import glob

#generate DDL to insert metrics (schema & tables)
#sql/base_tables
#sql/downstream_tables
#sql/exception_tables
def run_sql_queries_in_directory(directory,ini_file_name):
    conn = get_db_connection(ini_file_name)
    cur = conn.cursor()
    filelist = glob.glob(os.path.join(directory, '*.sql'))

    #execute all .sql files in sql folder
    for infile in sorted(filelist):
                print("starting " + infile)
                args = infile
                cur.execute(open(infile,"r").read())
                print("Complete!")
    conn.close()

