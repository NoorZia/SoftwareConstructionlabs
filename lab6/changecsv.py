import csv
import sys
lens={1:0,7:0,9:0}
rows = []
i=0
f = open("GeoLiteCity-Location1.csv", 'rt')

reader = csv.reader(f)
for row in reader:
    lens[len(row)]+=1

print lens       
"""i+=1
        if(i==2):
            continue
        if( len(row)==9):
            rows.append(row)
  
        lens[len(row)]+=1
finally:
    f.close()
lists = ['locId', 'country', 'region', 'city', 'postalCode', 'latitude', 'longitude', 'metroCode', 'areaCode']

print lens
print rows[:10]

for x in rows:
    print type(x)

    if(x[1]==''):
        x[1]='nocountry'
    if(x[2]==''):
	x[2]='noregion'
    if(x[3]==''):
	x[3]='nocity'
    if(x[4]==''):
	x[4]=123456789
	
    if(x[5]==''):
	x[5]=10000
    if(x[6]==''):
	x[6]=10000
    if(x[7]==''):
	x[7]=123456789
    if(x[8]==''):
	x[8]=123456789



f = open("GeoLiteCity-Location1.csv", 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('locId', 'country', 'region', 'city', 'postalCode', 'latitude', 'longitude', 'metroCode', 'areaCode') )
    for i in rows:
        writer.writerow( (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]) )
finally:
    f.close()
"""
