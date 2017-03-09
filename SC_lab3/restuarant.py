import os
import numpy
import pickle
"""
1. 1 extra-large table with max capacity of 12 people.
2. 3 large tables with max capacity of 6 people.
3. 8 medium tables with max capacity of 4 people.
4. 4 small tables with max capacity of 2 people.
"""
tables = {}
tables['exlarge'] = [1,12,1]
tables['large'] = [3,6,3]
tables['medium'] = [8,4,8]
tables['small'] = [4,2,4]
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


def booking_res():
    bookings,booking,all_tables = init()
    table_bookings={}
    table_bookings['large'] = [[] for x in range(0,3)]
    table_bookings['small'] = [[] for x in range(0,4)]
    table_bookings['medium'] = [[] for x in range(0,8)]
    table_bookings['exlarge'] = []
    with open('bookings.txt', "rb") as input_file:
        booking_list = pickle.load(input_file)
    print booking_list
    for i in booking_list:
        table_bookings[i[0]][i[3]] = (i[2],i[1])


    hour = 0
    if (booking==16):
        hour+=1

    t = raw_input("choose your table size? exlarge, large, small, medium")
    if(t not in tables.keys()):
        print "Wrong table size"
    elif(t!= "exlarge"):
        name = raw_input("Enter your name")
        time = int(raw_input("Choose your available time between "+str(hour+11)+ "hrs to "+str(hour+11+11)+ "hrs"))
        l = table_bookings[t]
        if(time < (hour+11) or time> (hour+11+11)):
            return "cannot book"

        found = 0
        frame = 1
        for idx,x in enumerate(l):

            if time not in x:
                for b in x:
                    if(abs(b-time)<1):
                        frame = 0

                table_bookings[t][idx].append((name,time))
                id = idx
                found = 1

                break
        if(found==1 and frame==1):

            booking_list.append((t,time,name,id))
            return booking_list

        else:
            return "table not booked"

    else:
        time = int(raw_input("Choose your available time between "+str(hour+11)+ "hrs to "+str(hour+11+11)+ "hrs"))
        duration = int(raw_input("Enter time duration"))
        name = raw_input("Enter your name")
        if(time < (hour+11) or time> (hour+11+11)):
            return "cannot book"
        if(time+duration > (hour+22)):
            return "time out of range"
        found = 0
        frame = 1
        for idx,x in enumerate(l):

            if time not in x:
                for b in x:
                    if(abs(b-time)<duration):
                        frame = 0


                table_bookings[t][idx].append((name,time))
                found = 1
                id = idx

                break
        if(found==1 and frame==1):

            booking_list.append((t,time,name,id))
            return booking_list
        else:
            return "table not booked"

    return bookings



def booking_test(t,name,time,duration=None):
    bookings,booking,all_tables = init()
    table_bookings={}
    table_bookings['large'] = [[] for x in range(0,3)]
    table_bookings['small'] = [[] for x in range(0,4)]
    table_bookings['medium'] = [[] for x in range(0,8)]
    table_bookings['exlarge'] = []
    with open('bookings.txt', "rb") as input_file:
        booking_list = pickle.load(input_file)
    print booking_list
    for i in booking_list:
        table_bookings[i[0]][i[3]] = (i[2],i[1])


    hour = 0

    if(t not in tables.keys()):
        return "false"
    elif(t!= "exlarge"):

        l = table_bookings[t]
        if(time < (hour+11) or time> (hour+11+11)):
            return "false"

        found = 0
        frame = 1
        for idx,x in enumerate(l):

            if time not in x:
                for b in x:
                    if(abs(b-time)<1):
                        frame = 0

                table_bookings[t][idx].append((name,time))
                id = idx
                found = 1

                break
        if(found==1 and frame==1):

            booking_list.append((t,time,name,id))
            if(type(booking_list)!='str'):
                with open('bookings.txt', 'w') as handle:
                    pickle.dump(booking_list, handle)
            return "true"

        else:
            return "false"

    else:

        if(time < (hour+11) or time> (hour+11+11)):
            return "false"
        if(time+duration > (hour+22)):
            return "false"
        found = 0
        frame = 1
        for idx,x in enumerate(l):

            if time not in x:
                for b in x:
                    if(abs(b-time)<duration):
                        frame = 0


                table_bookings[t][idx].append((name,time))
                found = 1
                id = idx

                break
        if(found==1 and frame==1):

            booking_list.append((t,time,name,id))
            if(type(booking_list)!='str'):
                with open('bookings.txt', 'w') as handle:
                    pickle.dump(booking_list, handle)
            return "true"
        else:
            return "false"

    return bookings
