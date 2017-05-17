# -*- coding: utf-8 -*-
import couchdb
import csv
import json
from datetime import datetime
from couchdb.mapping import Document, TextField, IntegerField, DateTimeField,  FloatField
from math import radians, cos, sin, asin, sqrt

def mk_int(s):

    s = s.strip()
    return float(s) if s else 0

def getKey(item):
    return item[0]

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km
class City(Document):
    id = IntegerField()
    country = TextField()
    city = TextField()
    region = TextField()
    postalcode = TextField()
    metrocode = TextField()
    longitude = FloatField()
    latitude = FloatField()
    areacode = TextField()
def db_insertion():
    couch = couchdb.Server()

    db = couch.create('lab10test') # newly created
    db = couch['lab10test']


    f = open("GeoLiteCity-Location.csv", 'rt')
    reader = csv.reader(f)
    i=0
    for x in reader:
        i+=1
        if(i<3):
            continue
        #print x
        if(i%100==0):
            print i
        try:
            """city = City(id=mk_int(x[0]),country=x[1].decode('utf-8'),region=x[2].decode('utf-8'),city=x[3].decode('utf-8'),
            postalcode=x[4].decode('utf-8'),latitude=mk_int(x[5]),longitude=mk_int(x[6])
            ,metrocode=x[7].decode('utf-8'),areacode=x[8].decode('utf-8'))"""
            city = City(city=x[3].decode('utf-8'),
            latitude=mk_int(x[5]),longitude=mk_int(x[6])
            )
            city.store(db)

        except UnicodeDecodeError:
            print "skipping"

def latlng(l1,l2,l3,l4):
    return haversine(l1,l2,l3,l4)

def city2city(city1,city2):
    couch = couchdb.Server()
    db = couch['lab10']
    rows = db.view('_all_docs',include_docs=True)
    docs = [row.doc for row in rows]
    data_retrieved={}
    i=0

    for x in db:
        i+=1
        #print x
        if(i<50):
            c = City.load(db,x)
            data_retrieved[c.city] = (c.latitude,c.longitude)

    u = data_retrieved.keys()

    return haversine(data_retrieved[city1][0],data_retrieved[city1][1],data_retrieved[city2][0],data_retrieved[city2][1])


def n_cities(city1,n):
    couch = couchdb.Server()
    db = couch['lab10']
    rows = db.view('_all_docs',include_docs=True)
    docs = [row.doc for row in rows]
    data_retrieved={}
    i=0

    for x in db:
        i+=1
        #print x
        if(i<50):
            c = City.load(db,x)
            data_retrieved[c.city] = (c.latitude,c.longitude)

    u = data_retrieved.keys()

    distances = []

    for o in u:
        distances.append((haversine(data_retrieved[city1][0],data_retrieved[city1][1],data_retrieved[o][0],data_retrieved[o][1]),o))
    distances = sorted(distances, key=getKey)

    return distances[1:n+1]

#########
def n_latlng(l1,l2,n):
    couch = couchdb.Server()
    db = couch['lab10']
    rows = db.view('_all_docs',include_docs=True)
    docs = [row.doc for row in rows]
    data_retrieved={}
    i=0

    for x in db:
        i+=1
        #print x
        if(i<50):
            c = City.load(db,x)
            data_retrieved[c.city] = (c.latitude,c.longitude)

    u = data_retrieved.keys()

    distances2=[]
    for o in u:
        distances2.append((haversine(l1,l2,data_retrieved[o][0],data_retrieved[o][1]),o))
    distances2 = sorted(distances2, key=getKey)
    return distances2[1:n+1]



#######
def ui():
    couch = couchdb.Server()
    db = couch['lab10']
    rows = db.view('_all_docs',include_docs=True)
    docs = [row.doc for row in rows]
    data_retrieved={}
    i=0

    for x in db:
        i+=1
        #print x
        if(i<50):
            c = City.load(db,x)
            data_retrieved[c.city] = (c.latitude,c.longitude)
    user_latitude1 = float(raw_input("enter latitude"))
    user_longitude1 = float(raw_input("enter longitude"))
    user_latitude2 = float(raw_input("enter latitude"))
    user_longitude2 = float(raw_input("enter longitude"))

    u = data_retrieved.keys()
    print u
    city1 = raw_input("city 1:")
    city2 = raw_input("city 2:")
    print "Lat lng distance=",haversine(data_retrieved[city1][0],data_retrieved[city1][1],data_retrieved[city2][0],data_retrieved[city2][1])
    print "Cities distance=",haversine(user_latitude1,user_longitude1,user_latitude2,user_longitude2)
    distances = []
    def getKey(item):
        return item[0]
    for o in u:
        distances.append((haversine(data_retrieved[city1][0],data_retrieved[city1][1],data_retrieved[o][0],data_retrieved[o][1]),o))
    distances = sorted(distances, key=getKey)
    n = int(raw_input("Number of cities:"))
    print distances[1:n+1]
    distances2=[]
    for o in u:
        distances2.append((haversine(user_latitude1,user_longitude1,data_retrieved[o][0],data_retrieved[o][1]),o))
    distances2 = sorted(distances2, key=getKey)
    print distances2[1:n+1]
#ui()
