#!/usr/bin/python
from os.path import abspath, join, dirname
from app import db, models 
import csv
import sys
full_path = lambda filename: abspath(join(dirname(__file__), filename))

#Remove old plants
oldPlants = models.Plant.query.all()
for p in oldPlants:
	db.session.delete(p)
db.session.commit()
print("Old Plants Deleted") 

f = sys.stdin.readlines()
reader = csv.reader(f)
rownum = 0
plants = []
for row in reader:
    if rownum == 0:
        header = row
    else:
        plants.append(row)
        commonName1 = plants[rownum-1][1]
        commonName2 = plants[rownum-1][2]
        fullCommonName = ""
        if not (commonName1==""):
        	fullCommonName = commonName1 + " " + commonName2
        elif not(commonName2==""):
        	fullCommonName = commonName2
        else:
        	fullCommonName = "N/A"
        scientificName = plants[rownum-1][3]
        if scientificName=="":
        	scientificName = "N/A"
        latitude = plants[rownum-1][57]
        if latitude == "":
        	latitude = 0
        longitude = plants[rownum-1][56]
        if longitude == "":
        	longitude = 0
        p = models.Plant(commonName = fullCommonName, latinName = scientificName, latitude = latitude, longitude = longitude)
        db.session.add(p)
    print (rownum)
    rownum += 1
db.session.commit()        