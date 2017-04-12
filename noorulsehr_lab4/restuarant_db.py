import os
import numpy
import pickle
import time as okay
import MySQLdb
import hashlib
import datetime
authentication = False
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="restuarant")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

"""
1. 1 extra-large table with max capacity of 12 people.
2. 3 large tables with max capacity of 6 people.
3. 8 medium tables with max capacity of 4 people.
4. 4 small tables with max capacity of 2 people.
"""


"""
Define the initial table values and available tables
Tables will be stored by key and values
Key will be the size and values will be (total, seating, available)
"""

tables = {}
tables['exlarge'] = [1,12,1]
tables['large'] = [3,6,3]
tables['medium'] = [8,4,8]
tables['small'] = [4,2,4]

"""
   Initialize the table values, sides, menu
   Returns total bookings, total tables and bookings
   """
def init():
    sides = 3
    main = 12
    desserts = 4
    soups = 2
    appetizers = 4
    tables = {}
    tables['exlarge'] = [1,12,1]
    tables['large'] = [3,6,3]
    tables['medium'] = [8,4,8]
    tables['small'] = [4,2,4]
    all_tables = [tables for x in range(0,11)]


    maxpeople = 0
    for x,y in tables.items():
        maxpeople += y[0]*y[1]

    bookings = []
    booking = 0

    return bookings,booking,all_tables

"""Books the restuarant by taking user input
User can give their own time and are given a duration of 1 min
It then saves the booked tables in a pickle file and loads from that file later"""

"""Test function for booking
It takes the booking values as parameters and returns true on successful booking
"""
def booking_test():
    hour=0
    datee = str(datetime.date.today())
    s = cur.execute("SELECT * FROM bookings where date = '"+datee+"'")
    
    bookings_list = []
    # print all the first cell of all the rows



    bookings,booking,all_tables = init()
    table_bookings={}
    table_bookings['large'] = [[] for x in range(0,3)]
    table_bookings['small'] = [[] for x in range(0,4)]
    table_bookings['medium'] = [[] for x in range(0,8)]
    table_bookings['exlarge'] = []


    for row in cur.fetchall():
        bookings_list.append(row)
    """

        table_bookings[row[3]][int(row[4])]=(row[0],int(row[1]),int(row[2]))



    if(t not in tables.keys()):
        return False
    elif(t!= "exlarge"):


        l = table_bookings[t]
        if(time < (hour+11) or time> (hour+11+11)):
            return False

        found = 0
        frame = 1




        for idx,x in enumerate(l):
            if(len(x)==0):

                s = cur.execute("INSERT INTO bookings(name, time, duration, table_name, table_id) VALUES (%s,%s,%s,%s,%s)",(name,time,str(1),t,str(0)) )
                db.commit()
                return True
            if time not in x:


                if(abs(x[1]-time)<1):
                    frame = 0
                id = idx
                found = 1

                break
        if(found==1 and frame==1):

            bookings_list.append((t,time,name,id))
            #cur.execute("INSERT INTO `bookings`(`name`, `time`, `duration`, `table_name`, `table_id`) VALUES (%s,%s,%s,%s,%s)",(name,time,1,t,id) )
            s = cur.execute("INSERT INTO bookings(name, time, duration, table_name, table_id) VALUES (%s,%s,%s,%s,%s)",(name,time,str(1),t,str(0)) )

            db.commit()
            return True


        else:
            return False

    else:
        #if table is ex large
        l = table_bookings[t]

        if(time < (hour+11) or time> (hour+11+11)):
            return False
        if(time+duration > (hour+22)):
            return False
        found = 0
        frame = 1

        #okay.sleep(300)
        if(len(l)==0):
            table_bookings[t].append((name,time,duration))
            id=0
            bookings_list.append((t,time,name,duration))
            return True

        else:
            for x in l:
                if time not in x:
                     if(abs(x[1]-time)<duration or abs((x[1]+x[2])-time)<duration ):
                        frame = 0
                table_bookings[t].append((name,time))
                id = idx
                found = 1

                break
        if(found==1 and frame==1):

            bookings_list.append((t,time,name,duration))
            s = cur.execute("INSERT INTO bookings(name, time, duration, table_name, table_id) VALUES (%s,%s,%s,%s,%s)",(name,time,str(duration),t,str(0)) )

            db.commit()


            return True   #booked successfully


        else:
            return False    #not booked
"""
booking_test()
