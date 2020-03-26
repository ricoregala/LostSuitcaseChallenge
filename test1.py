import xml.etree.ElementTree as ET
import requests, threading, json, os
from pprint import pprint as pprint
from dotenv import load_dotenv

load_dotenv()
ctabusapiKey = os.getenv("ctabusapiKey")

# root = ET.fromstring(requests.get('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22').text)
# busId = [data.find('id').text for data in root.findall('bus')]
# destination = [data.find('dd').text for data in root.findall('bus')]
# arrLat = [data.find('lat').text for data in root.findall('bus')]
# arrLon = [data.find('lon').text for data in root.findall('bus')]
# indexNorthboundbuses = [ i for i in range(len(destination)) if destination[i] == 'Northbound' ]
# arrlatlonJoined = [",".join([arrLat[indexNorthboundbuses[j]],arrLon[indexNorthboundbuses[j]]]) for j in range(len(indexNorthboundbuses))]
# originsJoin = ";".join(str(p) for p in arrlatlonJoined)


getPatterns = f"http://www.ctabustracker.com/bustime/api/v2/getpatterns?key={ctabusapiKey}&format=json&rt=22"
getVehicles = f"http://www.ctabustracker.com/bustime/api/v2/getvehicles?key={ctabusapiKey}&format=json&rt=22"
getStops = f"http://www.ctabustracker.com/bustime/api/v2/getstops?key={ctabusapiKey}&format=json&rt=22&dir=Northbound"
patternResponse = requests.get(getPatterns).json()
stopsResponse = requests.get(getStops).json()
# vehicleResp = requests.get(getVehicles).json()
# List the index of the patterns with route direction Northbound
totalPatterns = range(len(patternResponse["bustime-response"]["ptr"]))
# Using the List Comprehension syntax to shorten the code, get the index of Northbound Routes.
indexofnorthboundRoutes = [
    i
    for i in totalPatterns
    if patternResponse["bustime-response"]["ptr"][i]["rtdir"] == "Northbound"
]
totalRoutes = range(len(indexofnorthboundRoutes))


def patternFind(k):
    return patternResponse["bustime-response"]["ptr"][indexofnorthboundRoutes[k]]


# Using the List Comprehension syntax to shorten the code, get the total distance of each routes denoted in feet.
patternDistance = [patternFind(k)["ln"] for k in totalRoutes]
# Using the List Comprehension syntax to shorten the code, get the pattern IDs of Northbound Routes
pidValues = [patternFind(k)["pid"] for k in totalRoutes]
# Using the List Comprehension syntax to shorten the code, create a list for each route a list of latitudes
getsequencePatternLat = [
    [patternFind(k)["pt"][j]["lat"] for j in range(len(patternFind(k)["pt"]))]
    for k in totalRoutes
]
# Using the List Comprehension syntax to shorten the code, create a list for each route a list of longitudes
getsequencePatternLon = [
    [patternFind(k)["pt"][j]["lon"] for j in range(len(patternFind(k)["pt"]))]
    for k in totalRoutes
]
# Join the Lat and Lon for each PIDs separated by ',' and put each in a list and list each per PID
joinedLatLon = [
    [
        ",".join([str(getsequencePatternLat[k][j]), str(getsequencePatternLon[k][j])])
        for j in range(len(patternFind(k)["pt"]))
    ]
    for k in totalRoutes
]
# [[' '.join([a[h][i],b[h][i]]) for i in range(len(a[0]))] for h in range(len(a))]
# PUT THE JOINED LAT AND LON TO A STATIC MAP.
# GET THE BUS ON GETVEHICLES USING THE PIDVALUES VARIABLE

# TRACK THE BUS ON THE MAP

joinedstopLatLon = [
    ",".join(
        [
            str(stopsResponse["bustime-response"]["stops"][k]["lat"]),
            str(stopsResponse["bustime-response"]["stops"][k]["lon"]),
        ]
    )
    for k in range(len(stopsResponse["bustime-response"]["stops"]))
]
latlonCombined = ";".join(joinedstopLatLon)

print(latlonCombined)
# References Used:
# https://stackoverflow.com/questions/21507319/python-list-comprehension-list-of-lists
# https://stackoverflow.com/questions/51963942/python-list-comprehension-with-list-of-lists
# https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
# https://www.geeksforgeeks.org/python-map-function/
# geeksforgeeks.org/nested-list-comprehensions-in-python/
# https://automatetheboringstuff.com/chapter6/
# https://www.tutorialspoint.com/python3/python_functions.htm
# https://docs.python.org/3/library/functions.html
# https://nerdparadise.com/programming/pythononeline
#
