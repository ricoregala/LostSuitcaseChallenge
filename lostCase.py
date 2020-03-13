import xml.etree.ElementTree as ET
import requests, threading, json
from pprint import pprint as pprint

oldctaparseUrl = requests.get('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22').text
root = ET.fromstring(oldctaparseUrl)
ctabusDir = []
ctabusId = []
# for ctaKeys in root.iter("dd"):
#     ctabusDir.append(str(ctaKeys.text))
    
# for ctaKeysId in root.iter("id"):
#     ctabusId.append(str(ctaKeysId.text))
    
# oldctaJoined = zip(ctabusDir, ctabusId)
# print(oldctaJoined)
# Construct Chicago Transit API Response
ctaapiEndpoints = {
    "victor" : {
        "name" : "Victor",
        "latitude" : "41.980262",
        "longitude" :"-87.668452",
        },
    "endpoints" : [
        "gettime",
        "getvehicles",
        "getroutes",
        "getdirections",
        "getstops",
        "getpatterns",
        "getpredictions",
        "getservice",
        "getservicebulletins"
        ],
    "format" : "&format=json",
    "rt" : "&rt=22",
    "url" : [
        "http://www.ctabustracker.com/bustime/api/v2/",
        "?key=wF7xCmctHX4BfHSxnpuEDJZGH"
        ],
}

"""#
https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix
?origins={lat0,long0;lat1,lon1;latM,lonM}     --> stops
&destinations={lat0,lon0;lat1,lon1;latN,longN}  --> victor
&travelMode={travelMode}
&startTime={startTime}
&timeUnit={timeUnit}
&key={BingMapsAPIKey}
"""
bingmapsroutesapiEndpoints = {
    "url" : [
        "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix",
        "&travelMode=driving",
        "&key=Ao9ah3QkRfnF1HH3K2OFLwhEXUHijpLe0Jtos_vLelRzXBGc4eo9yKZVPoXhfMXV"
    ]
}

# ctaLink = ctaapiEndpoints["url"][0] + ctaapiEndpoints["endpoints"][5] + ctaapiEndpoints["url"][1] + ctaapiEndpoints["format"] + ctaapiEndpoints["rt"]
#bingmapsLink = bingmapsroutesapiEndpoints["url"][0] + "?origins=41.88309783935547,-87.62935638427734" + "&destinations=41.980262,-87.668452" + bingmapsroutesapiEndpoints["url"][1] + bingmapsroutesapiEndpoints["url"][2]
# res0 = requests.get(str(ctaLink))
#res1 = requests.get(str(bingmapsLink))
#pprint(res1.json())

ctaUrl = "".join([ctaapiEndpoints["url"][0], ctaapiEndpoints["endpoints"][1], ctaapiEndpoints["url"][1], ctaapiEndpoints["format"], ctaapiEndpoints["rt"]])
res0 = requests.get(str(ctaUrl)).json()
# print(json.dumps(res0, sort_keys=True, indent=4))
arrbusLat = []
arrbusLon = []
arrallLatLon = []
for x in range(len(res0["bustime-response"]["vehicle"])):
    arrbusLat.append(res0["bustime-response"]["vehicle"][x]["lat"])
    arrbusLon.append(res0["bustime-response"]["vehicle"][x]["lon"])
    arrallLatLon.append(",".join([arrbusLat[x],arrbusLon[x]]))
victorJoin = ",".join([ctaapiEndpoints["victor"]["latitude"],ctaapiEndpoints["victor"]["longitude"]])
originsJoin = ";".join(str(p) for p in arrallLatLon)
mapsUrl = "".join([bingmapsroutesapiEndpoints["url"][0], "?origins=",originsJoin, "&destinations=",victorJoin, bingmapsroutesapiEndpoints["url"][1], bingmapsroutesapiEndpoints["url"][2]])
res1 = requests.get(mapsUrl).json()
pprint(json.dumps(res1, sort_keys=True, indent=4))