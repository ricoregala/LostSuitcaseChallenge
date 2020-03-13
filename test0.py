import xml.etree.ElementTree as ET
import requests, threading, json, os
from pprint import pprint as pprint
from dotenv import load_dotenv
load_dotenv()

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
APIkey = os.getenv('bingapiKey')
mapsUrl = f'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins={originsJoin}&destinations={victorOrigin}&travelMode=driving&key={APIkey}'
res0 = requests.get(mapsUrl).json()
print(res0)
# pprint(json.dumps(res0, indent=4))
