import xml.etree.ElementTree as ET
import requests, threading, json
from pprint import pprint as pprint

#Parse API to get ID and Destination and only select buses with northbound route
root = ET.fromstring(requests.get('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22').text)
getNorthboundbuses = {}

busId = [data.find('id').text for data in root.findall('bus')]
destination = [data.find('dd').text for data in root.findall('bus')]
arrLat = [data.find('lat').text for data in root.findall('bus')]
arrLon = [data.find('lon').text for data in root.findall('bus')]
print(busId)
print(destination)
print(arrLat)
print(arrLon)

# Use the filtered northbound parsed lattitude and longitude as origin in maps 


# for destination, lat, lon in getNorthboundbuses.items():
#     if destination == 'Northbound':
#         selectId.append(busId)