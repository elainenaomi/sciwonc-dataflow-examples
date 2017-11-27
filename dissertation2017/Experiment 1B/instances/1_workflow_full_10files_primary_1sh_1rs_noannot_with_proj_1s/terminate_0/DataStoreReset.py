#!/usr/bin/env python

import os
import glob
import csv
import gzip
import psycopg2

PATH_TO_FILE = os.path.dirname(os.path.realpath(__file__))
file_list = glob.glob(PATH_TO_FILE+"/*.txt")

# Try to connect

try:
    conn=psycopg2.connect("host='172.31.28.89' dbname='google' user='postgres' password='enw1989'")
except:
    print "I am unable to connect to the database."

cursor = conn.cursor()


for filename in file_list:
    print filename

    for statement in file(filename).read().split(';'):

        if statement and not statement.isspace():
            print "STATEMENT: "+statement
            cursor.execute(statement)

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cursor.close()
conn.close()
