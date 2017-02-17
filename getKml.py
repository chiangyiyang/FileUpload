import csv
import simplekml

inputfile = csv.reader(open('pos.csv', 'r'))
kml = simplekml.Kml()

for row in inputfile:
    kml.newpoint(name=row[0], coords=[(row[3], row[2])])

kml.save('pos.kml')
