#!/usr/bin/python
import MySQLdb
import hashlib
authentication = False
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="restuarant")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()


username = raw_input("Username = ")
password = raw_input("Password = ")

password =  hashlib.md5(password).hexdigest()
# Use all the SQL you like
name="noor"
t="medium"
time = "12"
s = cur.execute("SELECT * FROM servers where username=%s and password=%s",(username,password))
s = cur.execute("INSERT INTO bookings(name, time, duration, table_name, table_id) VALUES (%s,%s,%s,%s,%s)",(name,time,str(1),t,str(0)) )
s = cur.execute("INSERT INTO servers VALUES('"+"noor"+"','"+"noor"+"')")
db.commit()
for row in cur.fetchall():
    authentication = True

def logs_data():
    if (authentication == True):
        print "\nLOGS DATA"
        f = open("logs.txt").readlines()
        for x in f:
            print x
    else:
        print "You are not authenticated"


def make_query():
    if (authentication == True):
        query_string = raw_input("Enter query_string = ")
        f = open("logs.txt",'a')
        f.write(query_string)
        s = cur.execute(query_string)
        # print all the first cell of all the rows
        for row in cur.fetchall():
            print row

    else:
        print "You are not authenticated"

logs_data()
make_query()
db.close()
