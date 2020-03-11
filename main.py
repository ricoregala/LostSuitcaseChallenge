import xml.etree.ElementTree as ET
import requests, threading, json
from pprint import pprint as pprint

#Parse API to get ID and Destination and only select buses with northbound route
root = ET.fromstring(requests.get('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22').text)
busId = [data.find('id').text for data in root.findall('bus')]
destination = [data.find('dd').text for data in root.findall('bus')]
arrLat = [data.find('lat').text for data in root.findall('bus')]
arrLon = [data.find('lon').text for data in root.findall('bus')]
indexNorthboundbuses = [ i for i in range(len(destination)) if destination[i] == 'Northbound' ]
arrlatlonJoined = [",".join([arrLat[indexNorthboundbuses[j]],arrLon[indexNorthboundbuses[j]]]) for j in range(len(indexNorthboundbuses))]
originsJoin = ";".join(str(p) for p in arrlatlonJoined)

#Use originsJoin and input it in bing maps
victorOrigin = '41.980262,-87.668452'
bingmapsAPIkey = 'Ao9ah3QkRfnF1HH3K2OFLwhEXUHijpLe0Jtos_vLelRzXBGc4eo9yKZVPoXhfMXV'
mapsUrl = f'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins={originsJoin}&destinations={victorOrigin}&travelMode=driving&key={bingmapsAPIkey}'
res0 = requests.get(mapsUrl).json()
print(json.dumps(res0))