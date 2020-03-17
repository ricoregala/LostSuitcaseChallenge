import xml.etree.ElementTree as ET
import requests, threading, json, os
from pprint import pprint as pprint
from dotenv import load_dotenv

load_dotenv()
ctabusapiKey = os.getenv('ctabusapiKey')

# root = ET.fromstring(requests.get('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22').text)
# busId = [data.find('id').text for data in root.findall('bus')]
# destination = [data.find('dd').text for data in root.findall('bus')]
# arrLat = [data.find('lat').text for data in root.findall('bus')]
# arrLon = [data.find('lon').text for data in root.findall('bus')]
# indexNorthboundbuses = [ i for i in range(len(destination)) if destination[i] == 'Northbound' ]
# arrlatlonJoined = [",".join([arrLat[indexNorthboundbuses[j]],arrLon[indexNorthboundbuses[j]]]) for j in range(len(indexNorthboundbuses))]
# originsJoin = ";".join(str(p) for p in arrlatlonJoined)


getPatterns = f'http://www.ctabustracker.com/bustime/api/v2/getpatterns?key={ctabusapiKey}&format=json&rt=22'
getVehicles = f'http://www.ctabustracker.com/bustime/api/v2/getvehicles?key={ctabusapiKey}&format=json&rt=22'
# patternResponse = requests.get(getPatterns).json()
# vehicleResp = requests.get(getVehicles).json()
# List the index of the patterns with route direction Northbound


cccc = '''
{
	"bustime-response": {
		"ptr": [
			{
				"pid": 3936,
				"ln": 57126.0,
				"rtdir": "Southbound",
				"pt": [
					{
						"seq": 1,
						"lat": 42.01892,
						"lon": -87.673292000001,
						"typ": "S",
						"stpid": "14096",
						"stpnm": "Paulina & Howard Terminal",
						"pdist": 0.0
					},
					{
						"seq": 2,
						"lat": 42.01888,
						"lon": -87.673418,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 3,
						"lat": 42.018998,
						"lon": -87.673625,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 4,
						"lat": 42.019169,
						"lon": -87.673727,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 5,
						"lat": 42.019357,
						"lon": -87.673725,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 6,
						"lat": 42.019397,
						"lon": -87.674165,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 7,
						"lat": 42.019372,
						"lon": -87.674355,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 8,
						"lat": 42.019388,
						"lon": -87.675087,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 9,
						"lat": 42.01938,
						"lon": -87.675373,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 10,
						"lat": 42.019388,
						"lon": -87.675643,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 11,
						"lat": 42.019372,
						"lon": -87.676072,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 12,
						"lat": 42.019388,
						"lon": -87.676295,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 13,
						"lat": 42.019293,
						"lon": -87.676311,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 14,
						"lat": 42.019197000001,
						"lon": -87.676327,
						"typ": "S",
						"stpid": "14056",
						"stpnm": "Clark & Howard",
						"pdist": 1015.0
					},
					{
						"seq": 15,
						"lat": 42.018197,
						"lon": -87.675898,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 16,
						"lat": 42.018117000001,
						"lon": -87.675865000002,
						"typ": "S",
						"stpid": "14091",
						"stpnm": "Clark & Birchwood",
						"pdist": 1427.0
					},
					{
						"seq": 17,
						"lat": 42.017275,
						"lon": -87.675485,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 18,
						"lat": 42.016288,
						"lon": -87.675325,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 19,
						"lat": 42.016217,
						"lon": -87.675309999999,
						"typ": "S",
						"stpid": "14057",
						"stpnm": "Clark & Rogers",
						"pdist": 2136.0
					},
					{
						"seq": 20,
						"lat": 42.015797,
						"lon": -87.675278,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 21,
						"lat": 42.015352,
						"lon": -87.675118,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 22,
						"lat": 42.015183,
						"lon": -87.67515,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 23,
						"lat": 42.014135,
						"lon": -87.67496,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 24,
						"lat": 42.014087000001,
						"lon": -87.674960000001,
						"typ": "S",
						"stpid": "1781",
						"stpnm": "Clark & Chase",
						"pdist": 2933.0
					},
					{
						"seq": 25,
						"lat": 42.013777,
						"lon": -87.674865,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 26,
						"lat": 42.012513,
						"lon": -87.674722,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 27,
						"lat": 42.012378000001,
						"lon": -87.674642,
						"typ": "S",
						"stpid": "14429",
						"stpnm": "Clark & Touhy",
						"pdist": 3566.0
					},
					{
						"seq": 28,
						"lat": 42.01206,
						"lon": -87.674627,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 29,
						"lat": 42.010598,
						"lon": -87.674329,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 30,
						"lat": 42.010423000001,
						"lon": -87.674292,
						"typ": "S",
						"stpid": "1784",
						"stpnm": "Clark & Greenleaf",
						"pdist": 4289.0
					},
					{
						"seq": 31,
						"lat": 42.009383,
						"lon": -87.674085,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 32,
						"lat": 42.009343,
						"lon": -87.674085000001,
						"typ": "S",
						"stpid": "1785",
						"stpnm": "Clark & Lunt",
						"pdist": 4690.0
					},
					{
						"seq": 33,
						"lat": 42.009048,
						"lon": -87.674038,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 34,
						"lat": 42.008858,
						"lon": -87.673943,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 35,
						"lat": 42.008112,
						"lon": -87.673815,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 36,
						"lat": 42.007982999999,
						"lon": -87.673782999998,
						"typ": "S",
						"stpid": "1786",
						"stpnm": "Clark & Morse",
						"pdist": 5197.0
					},
					{
						"seq": 37,
						"lat": 42.006387,
						"lon": -87.67337,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 38,
						"lat": 42.005115,
						"lon": -87.6731,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 39,
						"lat": 42.005027000001,
						"lon": -87.673020000002,
						"typ": "S",
						"stpid": "14430",
						"stpnm": "Clark & Pratt",
						"pdist": 6296.0
					},
					{
						"seq": 40,
						"lat": 42.003255,
						"lon": -87.672465,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 41,
						"lat": 42.003246999999,
						"lon": -87.672448000001,
						"typ": "S",
						"stpid": "17638",
						"stpnm": "Clark & North Shore",
						"pdist": 6964.0
					},
					{
						"seq": 42,
						"lat": 42.00209,
						"lon": -87.672035,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 43,
						"lat": 42.001951999999,
						"lon": -87.671987999999,
						"typ": "S",
						"stpid": "1790",
						"stpnm": "Clark & Albion",
						"pdist": 7451.0
					},
					{
						"seq": 44,
						"lat": 42.000283,
						"lon": -87.671352,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 45,
						"lat": 41.999973,
						"lon": -87.671272,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 46,
						"lat": 41.999892999999,
						"lon": -87.671272,
						"typ": "S",
						"stpid": "1791",
						"stpnm": "Clark & Arthur",
						"pdist": 8230.0
					},
					{
						"seq": 47,
						"lat": 41.998503,
						"lon": -87.670843,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 48,
						"lat": 41.998360000001,
						"lon": -87.670794999998,
						"typ": "S",
						"stpid": "1792",
						"stpnm": "Clark & Devon",
						"pdist": 8804.0
					},
					{
						"seq": 49,
						"lat": 41.9972,
						"lon": -87.670445,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 50,
						"lat": 41.996755,
						"lon": -87.670398,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 51,
						"lat": 41.996627999999,
						"lon": -87.670398000001,
						"typ": "S",
						"stpid": "1793",
						"stpnm": "Clark & Rosemont",
						"pdist": 9449.0
					},
					{
						"seq": 52,
						"lat": 41.996152,
						"lon": -87.670318,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 53,
						"lat": 41.994872,
						"lon": -87.670303,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 54,
						"lat": 41.99472,
						"lon": -87.670303000001,
						"typ": "S",
						"stpid": "1794",
						"stpnm": "Clark & Granville",
						"pdist": 10148.0
					},
					{
						"seq": 55,
						"lat": 41.99383,
						"lon": -87.670238,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 56,
						"lat": 41.993132,
						"lon": -87.670255,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 57,
						"lat": 41.993067000001,
						"lon": -87.670255,
						"typ": "S",
						"stpid": "1795",
						"stpnm": "Clark & Glenlake",
						"pdist": 10748.0
					},
					{
						"seq": 58,
						"lat": 41.99232,
						"lon": -87.67016,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 59,
						"lat": 41.99058,
						"lon": -87.670128,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 60,
						"lat": 41.990517000001,
						"lon": -87.670159999999,
						"typ": "S",
						"stpid": "15258",
						"stpnm": "Clark & Elmdale/Peterson",
						"pdist": 11682.0
					},
					{
						"seq": 61,
						"lat": 41.989642,
						"lon": -87.670128,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 62,
						"lat": 41.989492,
						"lon": -87.670128,
						"typ": "S",
						"stpid": "17155",
						"stpnm": "Clark & Ridge",
						"pdist": 12058.0
					},
					{
						"seq": 63,
						"lat": 41.988815,
						"lon": -87.67,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 64,
						"lat": 41.988347,
						"lon": -87.669953,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 65,
						"lat": 41.988292,
						"lon": -87.669953000002,
						"typ": "S",
						"stpid": "17156",
						"stpnm": "Clark & Thorndale",
						"pdist": 12506.0
					},
					{
						"seq": 66,
						"lat": 41.986304,
						"lon": -87.669461,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 67,
						"lat": 41.986145000001,
						"lon": -87.669412999999,
						"typ": "S",
						"stpid": "1799",
						"stpnm": "Clark & Edgewater",
						"pdist": 13303.0
					},
					{
						"seq": 68,
						"lat": 41.98597,
						"lon": -87.669397,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 69,
						"lat": 41.985613,
						"lon": -87.669238,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 70,
						"lat": 41.984055,
						"lon": -87.668888,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 71,
						"lat": 41.98342,
						"lon": -87.668808,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 72,
						"lat": 41.983307999999,
						"lon": -87.668777000001,
						"typ": "S",
						"stpid": "14786",
						"stpnm": "Clark & Bryn Mawr",
						"pdist": 14354.0
					},
					{
						"seq": 73,
						"lat": 41.983165,
						"lon": -87.668682,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 74,
						"lat": 41.981965,
						"lon": -87.668458,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 75,
						"lat": 41.981852999999,
						"lon": -87.668457999999,
						"typ": "S",
						"stpid": "1803",
						"stpnm": "Clark & Catalpa",
						"pdist": 14904.0
					},
					{
						"seq": 76,
						"lat": 41.980527,
						"lon": -87.668332,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 77,
						"lat": 41.979748,
						"lon": -87.668332,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 78,
						"lat": 41.979685000001,
						"lon": -87.668332000001,
						"typ": "S",
						"stpid": "14787",
						"stpnm": "Clark & Balmoral",
						"pdist": 15690.0
					},
					{
						"seq": 79,
						"lat": 41.97823,
						"lon": -87.66838,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 80,
						"lat": 41.978135000001,
						"lon": -87.668426999999,
						"typ": "S",
						"stpid": "1805",
						"stpnm": "Clark & Berwyn",
						"pdist": 16254.0
					},
					{
						"seq": 81,
						"lat": 41.97645,
						"lon": -87.66849,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 82,
						"lat": 41.976387000001,
						"lon": -87.668489999999,
						"typ": "S",
						"stpid": "1806",
						"stpnm": "Clark & Foster",
						"pdist": 16887.0
					},
					{
						"seq": 83,
						"lat": 41.97614,
						"lon": -87.66838,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 84,
						"lat": 41.97447,
						"lon": -87.668157,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 85,
						"lat": 41.973367,
						"lon": -87.668062,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 86,
						"lat": 41.973247,
						"lon": -87.668061999999,
						"typ": "S",
						"stpid": "14790",
						"stpnm": "Clark & Winnemac",
						"pdist": 18042.0
					},
					{
						"seq": 87,
						"lat": 41.97184,
						"lon": -87.667823,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 88,
						"lat": 41.971657000001,
						"lon": -87.667807000002,
						"typ": "S",
						"stpid": "14613",
						"stpnm": "Clark & Ainslie",
						"pdist": 18622.0
					},
					{
						"seq": 89,
						"lat": 41.971133,
						"lon": -87.667697,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 90,
						"lat": 41.970497,
						"lon": -87.66768,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 91,
						"lat": 41.969377,
						"lon": -87.667537,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 92,
						"lat": 41.968765,
						"lon": -87.667522,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 93,
						"lat": 41.968477999999,
						"lon": -87.667442000001,
						"typ": "S",
						"stpid": "14431",
						"stpnm": "Clark & Lawrence",
						"pdist": 19783.0
					},
					{
						"seq": 94,
						"lat": 41.967525,
						"lon": -87.667218,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 95,
						"lat": 41.967167,
						"lon": -87.667203,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 96,
						"lat": 41.967151999999,
						"lon": -87.667108000002,
						"typ": "S",
						"stpid": "1811",
						"stpnm": "Clark & Leland",
						"pdist": 20289.0
					},
					{
						"seq": 97,
						"lat": 41.965037,
						"lon": -87.66671,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 98,
						"lat": 41.964942,
						"lon": -87.666694999999,
						"typ": "S",
						"stpid": "15519",
						"stpnm": "Clark & Wilson",
						"pdist": 21097.0
					},
					{
						"seq": 99,
						"lat": 41.963727,
						"lon": -87.666425,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 100,
						"lat": 41.963557999999,
						"lon": -87.666377,
						"typ": "S",
						"stpid": "1813",
						"stpnm": "Clark & Sunnyside",
						"pdist": 21611.0
					},
					{
						"seq": 101,
						"lat": 41.9629,
						"lon": -87.666187,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 102,
						"lat": 41.961898,
						"lon": -87.666027,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 103,
						"lat": 41.961787000001,
						"lon": -87.666011999998,
						"typ": "S",
						"stpid": "1814",
						"stpnm": "Clark & Montrose",
						"pdist": 22268.0
					},
					{
						"seq": 104,
						"lat": 41.960055,
						"lon": -87.665312,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 105,
						"lat": 41.959943000001,
						"lon": -87.665297000002,
						"typ": "S",
						"stpid": "1815",
						"stpnm": "Clark & Cullom",
						"pdist": 22970.0
					},
					{
						"seq": 106,
						"lat": 41.959823,
						"lon": -87.665312,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 107,
						"lat": 41.957997,
						"lon": -87.664517,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 108,
						"lat": 41.957153,
						"lon": -87.66404,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 109,
						"lat": 41.957018000001,
						"lon": -87.663960000001,
						"typ": "S",
						"stpid": "14439",
						"stpnm": "Clark & Southport",
						"pdist": 24101.0
					},
					{
						"seq": 110,
						"lat": 41.955222,
						"lon": -87.6628,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 111,
						"lat": 41.95457,
						"lon": -87.662483,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 112,
						"lat": 41.954532000001,
						"lon": -87.66234,
						"typ": "S",
						"stpid": "1818",
						"stpnm": "Clark & Irving Park",
						"pdist": 25122.0
					},
					{
						"seq": 113,
						"lat": 41.953538,
						"lon": -87.661528,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 114,
						"lat": 41.953481999999,
						"lon": -87.661481999998,
						"typ": "S",
						"stpid": "1819",
						"stpnm": "3930 N Clark",
						"pdist": 25569.0
					},
					{
						"seq": 115,
						"lat": 41.952822,
						"lon": -87.66094,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 116,
						"lat": 41.952743000001,
						"lon": -87.660892999999,
						"typ": "S",
						"stpid": "1820",
						"stpnm": "Clark & Byron",
						"pdist": 25882.0
					},
					{
						"seq": 117,
						"lat": 41.952663,
						"lon": -87.660908,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 118,
						"lat": 41.951877,
						"lon": -87.660257,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 119,
						"lat": 41.950883,
						"lon": -87.659542,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 120,
						"lat": 41.950803,
						"lon": -87.659462999998,
						"typ": "S",
						"stpid": "14432",
						"stpnm": "Clark & Grace",
						"pdist": 26697.0
					},
					{
						"seq": 121,
						"lat": 41.950048,
						"lon": -87.658778,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 122,
						"lat": 41.949333,
						"lon": -87.65827,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 123,
						"lat": 41.949182999999,
						"lon": -87.658000000001,
						"typ": "S",
						"stpid": "1822",
						"stpnm": "Clark & Waveland",
						"pdist": 27417.0
					},
					{
						"seq": 124,
						"lat": 41.948658,
						"lon": -87.657523,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 125,
						"lat": 41.947752,
						"lon": -87.656808,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 126,
						"lat": 41.947458,
						"lon": -87.656633,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 127,
						"lat": 41.947426999999,
						"lon": -87.656617000002,
						"typ": "S",
						"stpid": "1823",
						"stpnm": "Clark & Addison",
						"pdist": 28164.0
					},
					{
						"seq": 128,
						"lat": 41.947045,
						"lon": -87.656252,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 129,
						"lat": 41.945813,
						"lon": -87.655282,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 130,
						"lat": 41.945709999999,
						"lon": -87.655218,
						"typ": "S",
						"stpid": "1824",
						"stpnm": "Clark & Cornelia",
						"pdist": 28894.0
					},
					{
						"seq": 131,
						"lat": 41.944065,
						"lon": -87.653915,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 132,
						"lat": 41.943787,
						"lon": -87.653757,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 133,
						"lat": 41.943769999999,
						"lon": -87.653662000001,
						"typ": "S",
						"stpid": "1826",
						"stpnm": "Clark & Roscoe",
						"pdist": 29728.0
					},
					{
						"seq": 134,
						"lat": 41.94323,
						"lon": -87.653152,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 135,
						"lat": 41.94199,
						"lon": -87.652198,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 136,
						"lat": 41.941974999999,
						"lon": -87.652197999999,
						"typ": "S",
						"stpid": "1827",
						"stpnm": "Clark & School/Aldine",
						"pdist": 30496.0
					},
					{
						"seq": 137,
						"lat": 41.941751,
						"lon": -87.652193,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 138,
						"lat": 41.940214,
						"lon": -87.65094,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 139,
						"lat": 41.940108000001,
						"lon": -87.650856999999,
						"typ": "S",
						"stpid": "1828",
						"stpnm": "Clark & Belmont",
						"pdist": 31279.0
					},
					{
						"seq": 140,
						"lat": 41.937855,
						"lon": -87.649032,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 141,
						"lat": 41.937738,
						"lon": -87.648940000001,
						"typ": "S",
						"stpid": "14895",
						"stpnm": "Clark & Barry/Halsted",
						"pdist": 32289.0
					},
					{
						"seq": 142,
						"lat": 41.93688,
						"lon": -87.648225,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 143,
						"lat": 41.936602,
						"lon": -87.64805,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 144,
						"lat": 41.936587,
						"lon": -87.64786,
						"typ": "S",
						"stpid": "1830",
						"stpnm": "Clark & Wellington",
						"pdist": 32819.0
					},
					{
						"seq": 145,
						"lat": 41.936332,
						"lon": -87.64759,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 146,
						"lat": 41.935665,
						"lon": -87.647033,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 147,
						"lat": 41.935052,
						"lon": -87.646603,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 148,
						"lat": 41.934987999999,
						"lon": -87.646572000002,
						"typ": "S",
						"stpid": "17751",
						"stpnm": "Clark & Orchard",
						"pdist": 33500.0
					},
					{
						"seq": 149,
						"lat": 41.934834,
						"lon": -87.646543,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 150,
						"lat": 41.932982,
						"lon": -87.645068,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 151,
						"lat": 41.932644,
						"lon": -87.644935,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 152,
						"lat": 41.932563,
						"lon": -87.644924999998,
						"typ": "S",
						"stpid": "18173",
						"stpnm": "Clark & Diversey",
						"pdist": 34502.0
					},
					{
						"seq": 153,
						"lat": 41.932265,
						"lon": -87.644833,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 154,
						"lat": 41.930908,
						"lon": -87.644075,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 155,
						"lat": 41.930781,
						"lon": -87.644004999999,
						"typ": "S",
						"stpid": "1834",
						"stpnm": "Clark & Drummond",
						"pdist": 35200.0
					},
					{
						"seq": 156,
						"lat": 41.930038,
						"lon": -87.643542,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 157,
						"lat": 41.929596,
						"lon": -87.642897,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 158,
						"lat": 41.928751,
						"lon": -87.642404,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 159,
						"lat": 41.928488000001,
						"lon": -87.642518000002,
						"typ": "S",
						"stpid": "1836",
						"stpnm": "Clark & Deming",
						"pdist": 36181.0
					},
					{
						"seq": 160,
						"lat": 41.928417,
						"lon": -87.642185,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 161,
						"lat": 41.927168,
						"lon": -87.64147,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 162,
						"lat": 41.927064999999,
						"lon": -87.641390000001,
						"typ": "S",
						"stpid": "1837",
						"stpnm": "Clark & Arlington",
						"pdist": 36810.0
					},
					{
						"seq": 163,
						"lat": 41.926103,
						"lon": -87.640787,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 164,
						"lat": 41.925658,
						"lon": -87.640563,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 165,
						"lat": 41.925602999999,
						"lon": -87.640737999999,
						"typ": "S",
						"stpid": "1838",
						"stpnm": "Clark & Fullerton",
						"pdist": 37422.0
					},
					{
						"seq": 166,
						"lat": 41.925675,
						"lon": -87.640453,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 167,
						"lat": 41.925372,
						"lon": -87.640198,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 168,
						"lat": 41.924102,
						"lon": -87.639483,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 169,
						"lat": 41.924022,
						"lon": -87.639403000001,
						"typ": "S",
						"stpid": "1839",
						"stpnm": "Clark & Belden",
						"pdist": 38172.0
					},
					{
						"seq": 170,
						"lat": 41.923878,
						"lon": -87.63926,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 171,
						"lat": 41.922948,
						"lon": -87.638657,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 172,
						"lat": 41.922313,
						"lon": -87.638323,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 173,
						"lat": 41.922232999999,
						"lon": -87.638306999999,
						"typ": "S",
						"stpid": "1840",
						"stpnm": "Clark & Webster",
						"pdist": 38892.0
					},
					{
						"seq": 174,
						"lat": 41.921852,
						"lon": -87.638433,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 175,
						"lat": 41.921573,
						"lon": -87.638212,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 176,
						"lat": 41.920302,
						"lon": -87.637465,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 177,
						"lat": 41.92019,
						"lon": -87.637416999999,
						"typ": "S",
						"stpid": "1841",
						"stpnm": "Clark & Dickens",
						"pdist": 39709.0
					},
					{
						"seq": 178,
						"lat": 41.920215,
						"lon": -87.63721,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 179,
						"lat": 41.91872,
						"lon": -87.636272,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 180,
						"lat": 41.918633,
						"lon": -87.636225000001,
						"typ": "S",
						"stpid": "14788",
						"stpnm": "Clark & Armitage",
						"pdist": 40401.0
					},
					{
						"seq": 181,
						"lat": 41.916893,
						"lon": -87.63516,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 182,
						"lat": 41.916725,
						"lon": -87.635065000001,
						"typ": "S",
						"stpid": "1843",
						"stpnm": "Clark & Wisconsin",
						"pdist": 41166.0
					},
					{
						"seq": 183,
						"lat": 41.916662,
						"lon": -87.635097,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 184,
						"lat": 41.916098,
						"lon": -87.634683,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 185,
						"lat": 41.91512,
						"lon": -87.63411,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 186,
						"lat": 41.914962000001,
						"lon": -87.633951999999,
						"typ": "S",
						"stpid": "1409",
						"stpnm": "Clark & Menomonee",
						"pdist": 41894.0
					},
					{
						"seq": 187,
						"lat": 41.914652,
						"lon": -87.633698,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 188,
						"lat": 41.913285,
						"lon": -87.632887,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 189,
						"lat": 41.913245,
						"lon": -87.632855,
						"typ": "S",
						"stpid": "1845",
						"stpnm": "Clark & W. Lasalle Drive",
						"pdist": 42593.0
					},
					{
						"seq": 190,
						"lat": 41.912252,
						"lon": -87.632188,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 191,
						"lat": 41.91175,
						"lon": -87.631902,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 192,
						"lat": 41.911448,
						"lon": -87.631807,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 193,
						"lat": 41.911298000001,
						"lon": -87.631741999999,
						"typ": "S",
						"stpid": "1846",
						"stpnm": "Clark & North Ave",
						"pdist": 43373.0
					},
					{
						"seq": 194,
						"lat": 41.911155,
						"lon": -87.631647,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 195,
						"lat": 41.91079,
						"lon": -87.631568,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 196,
						"lat": 41.909573,
						"lon": -87.6316,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 197,
						"lat": 41.909532999999,
						"lon": -87.6316,
						"typ": "S",
						"stpid": "1847",
						"stpnm": "Clark & Burton",
						"pdist": 44021.0
					},
					{
						"seq": 198,
						"lat": 41.908365,
						"lon": -87.63152,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 199,
						"lat": 41.908023,
						"lon": -87.631568,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 200,
						"lat": 41.907943000001,
						"lon": -87.631568,
						"typ": "S",
						"stpid": "1848",
						"stpnm": "Clark & Schiller",
						"pdist": 44600.0
					},
					{
						"seq": 201,
						"lat": 41.907507,
						"lon": -87.631503,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 202,
						"lat": 41.905982,
						"lon": -87.631488,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 203,
						"lat": 41.905924999999,
						"lon": -87.631488000001,
						"typ": "S",
						"stpid": "1849",
						"stpnm": "Clark & Goethe",
						"pdist": 45339.0
					},
					{
						"seq": 204,
						"lat": 41.905853,
						"lon": -87.6316,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 205,
						"lat": 41.904685,
						"lon": -87.63152,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 206,
						"lat": 41.904225,
						"lon": -87.631568,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 207,
						"lat": 41.904207999999,
						"lon": -87.631567999998,
						"typ": "S",
						"stpid": "1850",
						"stpnm": "Clark & Division (Red Line)",
						"pdist": 45981.0
					},
					{
						"seq": 208,
						"lat": 41.903413,
						"lon": -87.631488,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 209,
						"lat": 41.903327000001,
						"lon": -87.631519999999,
						"typ": "S",
						"stpid": "1851",
						"stpnm": "Clark & Elm",
						"pdist": 46306.0
					},
					{
						"seq": 210,
						"lat": 41.902833,
						"lon": -87.63152,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 211,
						"lat": 41.902103,
						"lon": -87.631615,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 212,
						"lat": 41.902078,
						"lon": -87.631615,
						"typ": "S",
						"stpid": "1852",
						"stpnm": "Clark & Maple",
						"pdist": 46762.0
					},
					{
						"seq": 213,
						"lat": 41.901768,
						"lon": -87.631568,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 214,
						"lat": 41.900792,
						"lon": -87.6316,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 215,
						"lat": 41.900768,
						"lon": -87.631600000001,
						"typ": "S",
						"stpid": "1853",
						"stpnm": "Clark & Oak",
						"pdist": 47240.0
					},
					{
						"seq": 216,
						"lat": 41.90029,
						"lon": -87.631503,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 217,
						"lat": 41.89952,
						"lon": -87.63152,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 218,
						"lat": 41.899457000001,
						"lon": -87.631519999998,
						"typ": "S",
						"stpid": "1854",
						"stpnm": "Clark & Delaware",
						"pdist": 47719.0
					},
					{
						"seq": 219,
						"lat": 41.899162,
						"lon": -87.631457,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 220,
						"lat": 41.898185,
						"lon": -87.631457,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 221,
						"lat": 41.898185,
						"lon": -87.631488000001,
						"typ": "S",
						"stpid": "1855",
						"stpnm": "Clark & Chestnut",
						"pdist": 48194.0
					},
					{
						"seq": 222,
						"lat": 41.897207,
						"lon": -87.631408,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 223,
						"lat": 41.897048,
						"lon": -87.63144,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 224,
						"lat": 41.896968,
						"lon": -87.63144,
						"typ": "S",
						"stpid": "1856",
						"stpnm": "Clark & Chicago",
						"pdist": 48640.0
					},
					{
						"seq": 225,
						"lat": 41.896773,
						"lon": -87.631267,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 226,
						"lat": 41.894815,
						"lon": -87.63121,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 227,
						"lat": 41.894760999999,
						"lon": -87.631207999999,
						"typ": "S",
						"stpid": "18255",
						"stpnm": "Clark & Huron",
						"pdist": 49460.0
					},
					{
						"seq": 228,
						"lat": 41.89197,
						"lon": -87.631192,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 229,
						"lat": 41.891842999999,
						"lon": -87.631187000001,
						"typ": "S",
						"stpid": "1859",
						"stpnm": "Clark & Grand",
						"pdist": 50525.0
					},
					{
						"seq": 230,
						"lat": 41.889542,
						"lon": -87.63111,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 231,
						"lat": 41.88945,
						"lon": -87.631106999999,
						"typ": "S",
						"stpid": "1861",
						"stpnm": "Clark & Kinzie",
						"pdist": 51398.0
					},
					{
						"seq": 232,
						"lat": 41.885403,
						"lon": -87.631026,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 233,
						"lat": 41.885319,
						"lon": -87.631141999999,
						"typ": "S",
						"stpid": "1864",
						"stpnm": "Clark & Lake",
						"pdist": 52915.0
					},
					{
						"seq": 234,
						"lat": 41.884316,
						"lon": -87.631087,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 235,
						"lat": 41.884141999999,
						"lon": -87.63109,
						"typ": "S",
						"stpid": "1865",
						"stpnm": "Clark & Randolph",
						"pdist": 53343.0
					},
					{
						"seq": 236,
						"lat": 41.881459,
						"lon": -87.630911,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 237,
						"lat": 41.881267000001,
						"lon": -87.630898000001,
						"typ": "S",
						"stpid": "15903",
						"stpnm": "Clark & Madison & Monroe",
						"pdist": 54393.0
					},
					{
						"seq": 238,
						"lat": 41.879176,
						"lon": -87.630779,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 239,
						"lat": 41.878985999999,
						"lon": -87.630768,
						"typ": "S",
						"stpid": "1869",
						"stpnm": "Clark & Adams",
						"pdist": 55221.0
					},
					{
						"seq": 240,
						"lat": 41.878502,
						"lon": -87.630699,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 241,
						"lat": 41.876534,
						"lon": -87.630608,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 242,
						"lat": 41.876767000001,
						"lon": -87.63063,
						"typ": "S",
						"stpid": "1871",
						"stpnm": "Clark & Van Buren",
						"pdist": 56155.0
					},
					{
						"seq": 243,
						"lat": 41.876313,
						"lon": -87.631107,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 244,
						"lat": 41.875885,
						"lon": -87.63117,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 245,
						"lat": 41.875702,
						"lon": -87.631107,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 246,
						"lat": 41.874168,
						"lon": -87.631027,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 247,
						"lat": 41.874065000001,
						"lon": -87.631027000001,
						"typ": "S",
						"stpid": "15895",
						"stpnm": "Clark & Harrison",
						"pdist": 57126.0
					}
				]
			},
			{
				"pid": 246,
				"ln": 58924.0,
				"rtdir": "Northbound",
				"pt": [
					{
						"seq": 1,
						"lat": 41.874065000001,
						"lon": -87.631027000001,
						"typ": "S",
						"stpid": "15895",
						"stpnm": "Clark & Harrison",
						"pdist": 0.0
					},
					{
						"seq": 2,
						"lat": 41.87386,
						"lon": -87.630709,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 3,
						"lat": 41.872299,
						"lon": -87.630635,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 4,
						"lat": 41.87224,
						"lon": -87.63049,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 5,
						"lat": 41.872255,
						"lon": -87.629301,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 6,
						"lat": 41.872293,
						"lon": -87.629098,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 7,
						"lat": 41.87263,
						"lon": -87.629078,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 8,
						"lat": 41.872704999999,
						"lon": -87.629079999998,
						"typ": "S",
						"stpid": "1875",
						"stpnm": "Dearborn & Polk",
						"pdist": 1259.0
					},
					{
						"seq": 9,
						"lat": 41.874787,
						"lon": -87.629154,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 10,
						"lat": 41.874857999999,
						"lon": -87.629155999998,
						"typ": "S",
						"stpid": "1876",
						"stpnm": "Dearborn & Harrison",
						"pdist": 2045.0
					},
					{
						"seq": 11,
						"lat": 41.875955,
						"lon": -87.629182,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 12,
						"lat": 41.876090000001,
						"lon": -87.629182000001,
						"typ": "S",
						"stpid": "1877",
						"stpnm": "Dearborn & Congress",
						"pdist": 2494.0
					},
					{
						"seq": 13,
						"lat": 41.877954,
						"lon": -87.629221,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 14,
						"lat": 41.878017999999,
						"lon": -87.629222999998,
						"typ": "S",
						"stpid": "14508",
						"stpnm": "Dearborn & Jackson",
						"pdist": 3197.0
					},
					{
						"seq": 15,
						"lat": 41.879771,
						"lon": -87.629292,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 16,
						"lat": 41.879886,
						"lon": -87.629297000001,
						"typ": "S",
						"stpid": "1880",
						"stpnm": "Dearborn & Adams",
						"pdist": 3879.0
					},
					{
						"seq": 17,
						"lat": 41.880983,
						"lon": -87.62931,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 18,
						"lat": 41.881117999999,
						"lon": -87.629312,
						"typ": "S",
						"stpid": "1881",
						"stpnm": "Dearborn & Monroe",
						"pdist": 4328.0
					},
					{
						"seq": 19,
						"lat": 41.882324,
						"lon": -87.629338,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 20,
						"lat": 41.882400999999,
						"lon": -87.629336999999,
						"typ": "S",
						"stpid": "1882",
						"stpnm": "Dearborn & Madison",
						"pdist": 4796.0
					},
					{
						"seq": 21,
						"lat": 41.883135,
						"lon": -87.629331,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 22,
						"lat": 41.883151,
						"lon": -87.628792,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 23,
						"lat": 41.883150999999,
						"lon": -87.628733999999,
						"typ": "S",
						"stpid": "14227",
						"stpnm": "Washington & State",
						"pdist": 5229.0
					},
					{
						"seq": 24,
						"lat": 41.883207,
						"lon": -87.62796,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 25,
						"lat": 41.883268,
						"lon": -87.627809,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 26,
						"lat": 41.884369,
						"lon": -87.627871,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 27,
						"lat": 41.884463,
						"lon": -87.627922,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 28,
						"lat": 41.884504,
						"lon": -87.628031,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 29,
						"lat": 41.884505,
						"lon": -87.628268,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 30,
						"lat": 41.884489,
						"lon": -87.629289,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 31,
						"lat": 41.884506,
						"lon": -87.629376,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 32,
						"lat": 41.884703,
						"lon": -87.629404,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 33,
						"lat": 41.884798000001,
						"lon": -87.629408,
						"typ": "S",
						"stpid": "1884",
						"stpnm": "Dearborn & Randolph",
						"pdist": 6433.0
					},
					{
						"seq": 34,
						"lat": 41.886223,
						"lon": -87.629449,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 35,
						"lat": 41.886351999999,
						"lon": -87.629452999999,
						"typ": "S",
						"stpid": "1885",
						"stpnm": "Dearborn Between Lake & Wacker (MB)",
						"pdist": 7000.0
					},
					{
						"seq": 36,
						"lat": 41.888216,
						"lon": -87.629469,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 37,
						"lat": 41.888308999999,
						"lon": -87.62947,
						"typ": "S",
						"stpid": "1887",
						"stpnm": "Dearborn & Marina City",
						"pdist": 7714.0
					},
					{
						"seq": 38,
						"lat": 41.889844,
						"lon": -87.629526,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 39,
						"lat": 41.889911999999,
						"lon": -87.629528,
						"typ": "S",
						"stpid": "15399",
						"stpnm": "Dearborn & Hubbard",
						"pdist": 8299.0
					},
					{
						"seq": 40,
						"lat": 41.891885,
						"lon": -87.629595,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 41,
						"lat": 41.89197,
						"lon": -87.62967,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 42,
						"lat": 41.891971000001,
						"lon": -87.629599000002,
						"typ": "S",
						"stpid": "14767",
						"stpnm": "Dearborn & Grand",
						"pdist": 9075.0
					},
					{
						"seq": 43,
						"lat": 41.89197,
						"lon": -87.62967,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 44,
						"lat": 41.892948,
						"lon": -87.629695,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 45,
						"lat": 41.893108,
						"lon": -87.629610999999,
						"typ": "S",
						"stpid": "1891",
						"stpnm": "Dearborn & Ontario",
						"pdist": 9514.0
					},
					{
						"seq": 46,
						"lat": 41.89311,
						"lon": -87.6297,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 47,
						"lat": 41.8968,
						"lon": -87.6298,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 48,
						"lat": 41.8968,
						"lon": -87.629704999999,
						"typ": "S",
						"stpid": "18447",
						"stpnm": "Dearborn & Chicago",
						"pdist": 10909.0
					},
					{
						"seq": 49,
						"lat": 41.8968,
						"lon": -87.6298,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 50,
						"lat": 41.898865,
						"lon": -87.629835,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 51,
						"lat": 41.898982,
						"lon": -87.629811,
						"typ": "S",
						"stpid": "1895",
						"stpnm": "Dearborn & Delaware",
						"pdist": 11733.0
					},
					{
						"seq": 52,
						"lat": 41.89898,
						"lon": -87.62983,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 53,
						"lat": 41.89981,
						"lon": -87.62987,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 54,
						"lat": 41.89979,
						"lon": -87.63097,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 55,
						"lat": 41.899893,
						"lon": -87.630967,
						"typ": "S",
						"stpid": "18412",
						"stpnm": "Walton & Dearborn",
						"pdist": 12379.0
					},
					{
						"seq": 56,
						"lat": 41.89979,
						"lon": -87.63097,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 57,
						"lat": 41.89979,
						"lon": -87.63133,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 58,
						"lat": 41.90045,
						"lon": -87.63135,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 59,
						"lat": 41.900455000001,
						"lon": -87.631294000002,
						"typ": "S",
						"stpid": "1897",
						"stpnm": "Clark & Oak",
						"pdist": 12771.0
					},
					{
						"seq": 60,
						"lat": 41.90045,
						"lon": -87.63135,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 61,
						"lat": 41.90171,
						"lon": -87.631294,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 62,
						"lat": 41.901775,
						"lon": -87.631279000002,
						"typ": "S",
						"stpid": "1898",
						"stpnm": "Clark & Maple",
						"pdist": 13268.0
					},
					{
						"seq": 63,
						"lat": 41.903618,
						"lon": -87.631294,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 64,
						"lat": 41.903763000001,
						"lon": -87.631255999998,
						"typ": "S",
						"stpid": "1899",
						"stpnm": "Clark & Division (Red Line)",
						"pdist": 13997.0
					},
					{
						"seq": 65,
						"lat": 41.90385,
						"lon": -87.631409,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 66,
						"lat": 41.90564,
						"lon": -87.631409,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 67,
						"lat": 41.905669999999,
						"lon": -87.631462000001,
						"typ": "S",
						"stpid": "1900",
						"stpnm": "Clark & Goethe",
						"pdist": 14723.0
					},
					{
						"seq": 68,
						"lat": 41.907593,
						"lon": -87.631454,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 69,
						"lat": 41.907742000001,
						"lon": -87.631432000002,
						"typ": "S",
						"stpid": "1901",
						"stpnm": "Clark & Schiller",
						"pdist": 15486.0
					},
					{
						"seq": 70,
						"lat": 41.908619,
						"lon": -87.631493,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 71,
						"lat": 41.909252,
						"lon": -87.631462,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 72,
						"lat": 41.909373999999,
						"lon": -87.631455,
						"typ": "S",
						"stpid": "1902",
						"stpnm": "Clark & Burton",
						"pdist": 16081.0
					},
					{
						"seq": 73,
						"lat": 41.909336,
						"lon": -87.631562,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 74,
						"lat": 41.911255,
						"lon": -87.631609,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 75,
						"lat": 41.911424,
						"lon": -87.631695,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 76,
						"lat": 41.911512000001,
						"lon": -87.631646999999,
						"typ": "S",
						"stpid": "15417",
						"stpnm": "Clark & North Avenue",
						"pdist": 16902.0
					},
					{
						"seq": 77,
						"lat": 41.913384,
						"lon": -87.632913,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 78,
						"lat": 41.913547,
						"lon": -87.633029999999,
						"typ": "S",
						"stpid": "1451",
						"stpnm": "Clark & Lasalle",
						"pdist": 17730.0
					},
					{
						"seq": 79,
						"lat": 41.915438,
						"lon": -87.634143,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 80,
						"lat": 41.915564999999,
						"lon": -87.634193000002,
						"typ": "S",
						"stpid": "1905",
						"stpnm": "Clark & Lincoln",
						"pdist": 18531.0
					},
					{
						"seq": 81,
						"lat": 41.916552,
						"lon": -87.634827,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 82,
						"lat": 41.916687,
						"lon": -87.634904999998,
						"typ": "S",
						"stpid": "1906",
						"stpnm": "Clark & Wisconsin",
						"pdist": 18987.0
					},
					{
						"seq": 83,
						"lat": 41.918243,
						"lon": -87.63586,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 84,
						"lat": 41.918355,
						"lon": -87.636176999999,
						"typ": "S",
						"stpid": "1907",
						"stpnm": "Clark & Armitage",
						"pdist": 19711.0
					},
					{
						"seq": 85,
						"lat": 41.91915,
						"lon": -87.636797,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 86,
						"lat": 41.919905,
						"lon": -87.637258,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 87,
						"lat": 41.920047999999,
						"lon": -87.637304999999,
						"typ": "S",
						"stpid": "1908",
						"stpnm": "Clark & Dickens",
						"pdist": 20402.0
					},
					{
						"seq": 88,
						"lat": 41.920302,
						"lon": -87.637512,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 89,
						"lat": 41.921828,
						"lon": -87.638402,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 90,
						"lat": 41.921875,
						"lon": -87.638402000001,
						"typ": "S",
						"stpid": "1909",
						"stpnm": "Clark & Webster",
						"pdist": 21134.0
					},
					{
						"seq": 91,
						"lat": 41.922122,
						"lon": -87.638608,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 92,
						"lat": 41.922822,
						"lon": -87.639038,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 93,
						"lat": 41.923632,
						"lon": -87.639435,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 94,
						"lat": 41.923648,
						"lon": -87.639451999999,
						"typ": "S",
						"stpid": "1910",
						"stpnm": "Clark & Belden",
						"pdist": 21849.0
					},
					{
						"seq": 95,
						"lat": 41.925283,
						"lon": -87.640428,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 96,
						"lat": 41.925437000001,
						"lon": -87.640516999999,
						"typ": "S",
						"stpid": "1911",
						"stpnm": "Clark & Fullerton",
						"pdist": 22561.0
					},
					{
						"seq": 97,
						"lat": 41.926856,
						"lon": -87.641209,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 98,
						"lat": 41.927032999999,
						"lon": -87.641295,
						"typ": "S",
						"stpid": "17266",
						"stpnm": "Clark & Arlington",
						"pdist": 23182.0
					},
					{
						"seq": 99,
						"lat": 41.928494,
						"lon": -87.642143,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 100,
						"lat": 41.928542999999,
						"lon": -87.642408,
						"typ": "S",
						"stpid": "1913",
						"stpnm": "Clark & Deming",
						"pdist": 23806.0
					},
					{
						"seq": 101,
						"lat": 41.929559,
						"lon": -87.64276,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 102,
						"lat": 41.930016,
						"lon": -87.643429,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 103,
						"lat": 41.930185,
						"lon": -87.643572,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 104,
						"lat": 41.930787,
						"lon": -87.643899,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 105,
						"lat": 41.930824999999,
						"lon": -87.643918,
						"typ": "S",
						"stpid": "1915",
						"stpnm": "Clark & Drummond",
						"pdist": 24758.0
					},
					{
						"seq": 106,
						"lat": 41.931698,
						"lon": -87.644456,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 107,
						"lat": 41.932139,
						"lon": -87.644697,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 108,
						"lat": 41.932825,
						"lon": -87.644908,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 109,
						"lat": 41.933097,
						"lon": -87.645142,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 110,
						"lat": 41.933128000001,
						"lon": -87.645172999999,
						"typ": "S",
						"stpid": "1917",
						"stpnm": "Clark & Diversey",
						"pdist": 25677.0
					},
					{
						"seq": 111,
						"lat": 41.933263,
						"lon": -87.645332,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 112,
						"lat": 41.934535,
						"lon": -87.646333,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 113,
						"lat": 41.934583000001,
						"lon": -87.646397000001,
						"typ": "S",
						"stpid": "1918",
						"stpnm": "Clark & Surf",
						"pdist": 26302.0
					},
					{
						"seq": 114,
						"lat": 41.934822,
						"lon": -87.64635,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 115,
						"lat": 41.934965,
						"lon": -87.646508,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 116,
						"lat": 41.936618,
						"lon": -87.64778,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 117,
						"lat": 41.936690000001,
						"lon": -87.647843,
						"typ": "S",
						"stpid": "14919",
						"stpnm": "Clark & Wellington",
						"pdist": 27183.0
					},
					{
						"seq": 118,
						"lat": 41.937072,
						"lon": -87.648257,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 119,
						"lat": 41.937787,
						"lon": -87.648828,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 120,
						"lat": 41.937897,
						"lon": -87.648972,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 121,
						"lat": 41.93858,
						"lon": -87.649465,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 122,
						"lat": 41.93874,
						"lon": -87.649608,
						"typ": "S",
						"stpid": "14437",
						"stpnm": "Clark & Barry/Halsted",
						"pdist": 28074.0
					},
					{
						"seq": 123,
						"lat": 41.939725,
						"lon": -87.650355,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 124,
						"lat": 41.939757,
						"lon": -87.650497999998,
						"typ": "S",
						"stpid": "1921",
						"stpnm": "Clark & Belmont",
						"pdist": 28530.0
					},
					{
						"seq": 125,
						"lat": 41.940162,
						"lon": -87.650927,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 126,
						"lat": 41.941473,
						"lon": -87.651945,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 127,
						"lat": 41.941616999999,
						"lon": -87.652008,
						"typ": "S",
						"stpid": "1922",
						"stpnm": "Clark & School/Aldine",
						"pdist": 29327.0
					},
					{
						"seq": 128,
						"lat": 41.941707,
						"lon": -87.652023,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 129,
						"lat": 41.943658,
						"lon": -87.653613,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 130,
						"lat": 41.943711000001,
						"lon": -87.653655,
						"typ": "S",
						"stpid": "18083",
						"stpnm": "Clark & Roscoe",
						"pdist": 30214.0
					},
					{
						"seq": 131,
						"lat": 41.944825,
						"lon": -87.654499,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 132,
						"lat": 41.944915,
						"lon": -87.654502999998,
						"typ": "S",
						"stpid": "14434",
						"stpnm": "Clark & Newport/Sheffield",
						"pdist": 30713.0
					},
					{
						"seq": 133,
						"lat": 41.947005,
						"lon": -87.6563,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 134,
						"lat": 41.947108000001,
						"lon": -87.656363000001,
						"typ": "S",
						"stpid": "1926",
						"stpnm": "Clark & Addison",
						"pdist": 31659.0
					},
					{
						"seq": 135,
						"lat": 41.94857,
						"lon": -87.657555,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 136,
						"lat": 41.949118,
						"lon": -87.657953,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 137,
						"lat": 41.94923,
						"lon": -87.658048,
						"typ": "S",
						"stpid": "18033",
						"stpnm": "Clark & Waveland",
						"pdist": 32560.0
					},
					{
						"seq": 138,
						"lat": 41.9508,
						"lon": -87.65932,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 139,
						"lat": 41.950907000001,
						"lon": -87.659414999998,
						"typ": "S",
						"stpid": "14438",
						"stpnm": "Clark & Grace",
						"pdist": 33278.0
					},
					{
						"seq": 140,
						"lat": 41.952635,
						"lon": -87.660814,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 141,
						"lat": 41.952758000001,
						"lon": -87.660893000001,
						"typ": "S",
						"stpid": "1929",
						"stpnm": "Clark & Byron",
						"pdist": 34063.0
					},
					{
						"seq": 142,
						"lat": 41.953283,
						"lon": -87.661353,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 143,
						"lat": 41.954555,
						"lon": -87.662277,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 144,
						"lat": 41.954672999999,
						"lon": -87.662340000001,
						"typ": "S",
						"stpid": "6281",
						"stpnm": "Clark & Irving Park",
						"pdist": 34864.0
					},
					{
						"seq": 145,
						"lat": 41.954825,
						"lon": -87.662483,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 146,
						"lat": 41.956407,
						"lon": -87.663437,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 147,
						"lat": 41.956565,
						"lon": -87.663515,
						"typ": "S",
						"stpid": "1931",
						"stpnm": "Clark & Belle Plaine",
						"pdist": 35624.0
					},
					{
						"seq": 148,
						"lat": 41.957018,
						"lon": -87.66385,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 149,
						"lat": 41.957337,
						"lon": -87.663993,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 150,
						"lat": 41.957431999999,
						"lon": -87.664057000001,
						"typ": "S",
						"stpid": "15541",
						"stpnm": "Clark & Southport",
						"pdist": 35977.0
					},
					{
						"seq": 151,
						"lat": 41.958043,
						"lon": -87.664438,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 152,
						"lat": 41.959197,
						"lon": -87.664978,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 153,
						"lat": 41.95972,
						"lon": -87.665153,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 154,
						"lat": 41.959777000001,
						"lon": -87.665152999998,
						"typ": "S",
						"stpid": "1933",
						"stpnm": "Clark & Cullom",
						"pdist": 36885.0
					},
					{
						"seq": 155,
						"lat": 41.959855,
						"lon": -87.665263,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 156,
						"lat": 41.961525,
						"lon": -87.6659,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 157,
						"lat": 41.961843,
						"lon": -87.665963,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 158,
						"lat": 41.961946999999,
						"lon": -87.665995,
						"typ": "S",
						"stpid": "15518",
						"stpnm": "Clark & Montrose",
						"pdist": 37714.0
					},
					{
						"seq": 159,
						"lat": 41.963178,
						"lon": -87.66625,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 160,
						"lat": 41.963353000001,
						"lon": -87.666297000001,
						"typ": "S",
						"stpid": "1935",
						"stpnm": "Clark & Sunnyside",
						"pdist": 38234.0
					},
					{
						"seq": 161,
						"lat": 41.963678,
						"lon": -87.666408,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 162,
						"lat": 41.965077,
						"lon": -87.666647,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 163,
						"lat": 41.965187999999,
						"lon": -87.666662999999,
						"typ": "S",
						"stpid": "1936",
						"stpnm": "Clark & Wilson",
						"pdist": 38919.0
					},
					{
						"seq": 164,
						"lat": 41.965903,
						"lon": -87.666885,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 165,
						"lat": 41.966928,
						"lon": -87.66706,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 166,
						"lat": 41.966985,
						"lon": -87.66706,
						"typ": "S",
						"stpid": "1937",
						"stpnm": "Clark & Leland",
						"pdist": 39584.0
					},
					{
						"seq": 167,
						"lat": 41.967485,
						"lon": -87.667218,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 168,
						"lat": 41.968573,
						"lon": -87.667442,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 169,
						"lat": 41.969115,
						"lon": -87.66749,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 170,
						"lat": 41.969129999999,
						"lon": -87.667489999999,
						"typ": "S",
						"stpid": "17395",
						"stpnm": "Clark & Lawrence",
						"pdist": 40374.0
					},
					{
						"seq": 171,
						"lat": 41.969288,
						"lon": -87.667568,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 172,
						"lat": 41.971625,
						"lon": -87.667775,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 173,
						"lat": 41.971722,
						"lon": -87.667807,
						"typ": "S",
						"stpid": "1939",
						"stpnm": "Clark & Ainslie",
						"pdist": 41323.0
					},
					{
						"seq": 174,
						"lat": 41.973517,
						"lon": -87.668093,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 175,
						"lat": 41.973683000001,
						"lon": -87.668109999999,
						"typ": "S",
						"stpid": "14789",
						"stpnm": "Clark & Winnemac",
						"pdist": 42039.0
					},
					{
						"seq": 176,
						"lat": 41.973843,
						"lon": -87.668205,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 177,
						"lat": 41.975988,
						"lon": -87.668412,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 178,
						"lat": 41.975997,
						"lon": -87.66838,
						"typ": "S",
						"stpid": "1942",
						"stpnm": "Clark & Foster",
						"pdist": 42896.0
					},
					{
						"seq": 179,
						"lat": 41.977317,
						"lon": -87.66838,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 180,
						"lat": 41.977762,
						"lon": -87.668332,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 181,
						"lat": 41.977848,
						"lon": -87.668332,
						"typ": "S",
						"stpid": "1943",
						"stpnm": "Clark & Berwyn",
						"pdist": 43570.0
					},
					{
						"seq": 182,
						"lat": 41.978317,
						"lon": -87.66838,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 183,
						"lat": 41.979955,
						"lon": -87.668283,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 184,
						"lat": 41.980050000001,
						"lon": -87.668283000001,
						"typ": "S",
						"stpid": "14791",
						"stpnm": "Clark & Balmoral",
						"pdist": 44360.0
					},
					{
						"seq": 185,
						"lat": 41.9802,
						"lon": -87.668363,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 186,
						"lat": 41.9814,
						"lon": -87.668427,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 187,
						"lat": 41.981497,
						"lon": -87.668426999999,
						"typ": "S",
						"stpid": "1945",
						"stpnm": "Clark & Catalpa",
						"pdist": 44897.0
					},
					{
						"seq": 188,
						"lat": 41.9816,
						"lon": -87.66838,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 189,
						"lat": 41.982783,
						"lon": -87.668602,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 190,
						"lat": 41.983595,
						"lon": -87.668682,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 191,
						"lat": 41.983658000001,
						"lon": -87.668697000001,
						"typ": "S",
						"stpid": "14792",
						"stpnm": "Clark & Bryn Mawr",
						"pdist": 45690.0
					},
					{
						"seq": 192,
						"lat": 41.985112,
						"lon": -87.669015,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 193,
						"lat": 41.985254999999,
						"lon": -87.669175000001,
						"typ": "S",
						"stpid": "1948",
						"stpnm": "Clark & Hollywood",
						"pdist": 46295.0
					},
					{
						"seq": 194,
						"lat": 41.98539,
						"lon": -87.669095,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 195,
						"lat": 41.986415,
						"lon": -87.669428,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 196,
						"lat": 41.98729,
						"lon": -87.669572,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 197,
						"lat": 41.987672,
						"lon": -87.669555,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 198,
						"lat": 41.98814,
						"lon": -87.66962,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 199,
						"lat": 41.988172000001,
						"lon": -87.669620000001,
						"typ": "S",
						"stpid": "1950",
						"stpnm": "Clark & Ardmore",
						"pdist": 47376.0
					},
					{
						"seq": 200,
						"lat": 41.988482,
						"lon": -87.669698,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 201,
						"lat": 41.98911,
						"lon": -87.66973,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 202,
						"lat": 41.989259999999,
						"lon": -87.669746999999,
						"typ": "S",
						"stpid": "1951",
						"stpnm": "Clark & Ridge",
						"pdist": 47775.0
					},
					{
						"seq": 203,
						"lat": 41.989952,
						"lon": -87.669827,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 204,
						"lat": 41.990468,
						"lon": -87.66981,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 205,
						"lat": 41.990683,
						"lon": -87.669905,
						"typ": "S",
						"stpid": "1952",
						"stpnm": "Clark & Elmdale/Peterson",
						"pdist": 48298.0
					},
					{
						"seq": 206,
						"lat": 41.990985,
						"lon": -87.669953,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 207,
						"lat": 41.992408,
						"lon": -87.669953,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 208,
						"lat": 41.992517999999,
						"lon": -87.669905000001,
						"typ": "S",
						"stpid": "1953",
						"stpnm": "Clark & Glenlake",
						"pdist": 48973.0
					},
					{
						"seq": 209,
						"lat": 41.993592,
						"lon": -87.67,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 210,
						"lat": 41.994562,
						"lon": -87.67,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 211,
						"lat": 41.994728,
						"lon": -87.670000000001,
						"typ": "S",
						"stpid": "17218",
						"stpnm": "Clark & Granville",
						"pdist": 49778.0
					},
					{
						"seq": 212,
						"lat": 41.99542,
						"lon": -87.670065,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 213,
						"lat": 41.99608,
						"lon": -87.670048,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 214,
						"lat": 41.996293,
						"lon": -87.670080000001,
						"typ": "S",
						"stpid": "1955",
						"stpnm": "Clark & Rosemont",
						"pdist": 50351.0
					},
					{
						"seq": 215,
						"lat": 41.997812,
						"lon": -87.670382,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 216,
						"lat": 41.997915,
						"lon": -87.670398000001,
						"typ": "S",
						"stpid": "1956",
						"stpnm": "Clark & Devon",
						"pdist": 50955.0
					},
					{
						"seq": 217,
						"lat": 41.99805,
						"lon": -87.67051,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 218,
						"lat": 42.000085,
						"lon": -87.671193,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 219,
						"lat": 42.000154999999,
						"lon": -87.671224999999,
						"typ": "S",
						"stpid": "1957",
						"stpnm": "Clark & Arthur",
						"pdist": 51805.0
					},
					{
						"seq": 220,
						"lat": 42.001443,
						"lon": -87.671702,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 221,
						"lat": 42.001594999999,
						"lon": -87.671717000002,
						"typ": "S",
						"stpid": "1958",
						"stpnm": "Clark & Albion",
						"pdist": 52346.0
					},
					{
						"seq": 222,
						"lat": 42.003398,
						"lon": -87.672353,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 223,
						"lat": 42.003438,
						"lon": -87.672368000002,
						"typ": "S",
						"stpid": "1959",
						"stpnm": "Clark & North Shore",
						"pdist": 53047.0
					},
					{
						"seq": 224,
						"lat": 42.003843,
						"lon": -87.672543,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 225,
						"lat": 42.005433,
						"lon": -87.673005,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 226,
						"lat": 42.005519999999,
						"lon": -87.673020000002,
						"typ": "S",
						"stpid": "14436",
						"stpnm": "Clark & Pratt",
						"pdist": 53832.0
					},
					{
						"seq": 227,
						"lat": 42.005687,
						"lon": -87.673132,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 228,
						"lat": 42.007093,
						"lon": -87.673465,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 229,
						"lat": 42.007888,
						"lon": -87.673577,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 230,
						"lat": 42.007905000001,
						"lon": -87.673576999999,
						"typ": "S",
						"stpid": "14785",
						"stpnm": "Clark & Morse",
						"pdist": 54708.0
					},
					{
						"seq": 231,
						"lat": 42.008692,
						"lon": -87.673799,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 232,
						"lat": 42.008867,
						"lon": -87.673877999999,
						"typ": "S",
						"stpid": "1963",
						"stpnm": "Clark & Lunt",
						"pdist": 55067.0
					},
					{
						"seq": 233,
						"lat": 42.01017,
						"lon": -87.674165,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 234,
						"lat": 42.010320000001,
						"lon": -87.674181999998,
						"typ": "S",
						"stpid": "17219",
						"stpnm": "Clark & Greenleaf",
						"pdist": 55606.0
					},
					{
						"seq": 235,
						"lat": 42.011448,
						"lon": -87.674403,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 236,
						"lat": 42.013015,
						"lon": -87.674578,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 237,
						"lat": 42.013102000001,
						"lon": -87.67461,
						"typ": "S",
						"stpid": "14463",
						"stpnm": "Clark & Touhy",
						"pdist": 56624.0
					},
					{
						"seq": 238,
						"lat": 42.013173,
						"lon": -87.67469,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 239,
						"lat": 42.013452,
						"lon": -87.674737,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 240,
						"lat": 42.013586999999,
						"lon": -87.674768,
						"typ": "S",
						"stpid": "1967",
						"stpnm": "Clark & Chase",
						"pdist": 56811.0
					},
					{
						"seq": 241,
						"lat": 42.014962,
						"lon": -87.67504,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 242,
						"lat": 42.01574,
						"lon": -87.675087,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 243,
						"lat": 42.015820000001,
						"lon": -87.675117999998,
						"typ": "S",
						"stpid": "1968",
						"stpnm": "Clark & Jarvis",
						"pdist": 57635.0
					},
					{
						"seq": 244,
						"lat": 42.015892,
						"lon": -87.67515,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 245,
						"lat": 42.016027,
						"lon": -87.675087,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 246,
						"lat": 42.016598,
						"lon": -87.673895,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 247,
						"lat": 42.016638,
						"lon": -87.673815000001,
						"typ": "S",
						"stpid": "15452",
						"stpnm": "Rogers & Hermitage",
						"pdist": 58122.0
					},
					{
						"seq": 248,
						"lat": 42.016693,
						"lon": -87.673927,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 249,
						"lat": 42.017043,
						"lon": -87.67318,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 250,
						"lat": 42.017172,
						"lon": -87.673005,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 251,
						"lat": 42.017345,
						"lon": -87.672957,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 252,
						"lat": 42.018387,
						"lon": -87.672957,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 253,
						"lat": 42.018427,
						"lon": -87.672956999998,
						"typ": "W",
						"pdist": 0.0
					}
				]
			},
			{
				"pid": 3932,
				"ln": 58208.0,
				"rtdir": "Northbound",
				"pt": [
					{
						"seq": 1,
						"lat": 41.874065000001,
						"lon": -87.631027000001,
						"typ": "S",
						"stpid": "15895",
						"stpnm": "Clark & Harrison",
						"pdist": 0.0
					},
					{
						"seq": 2,
						"lat": 41.87386,
						"lon": -87.630709,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 3,
						"lat": 41.872299,
						"lon": -87.630635,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 4,
						"lat": 41.87224,
						"lon": -87.63049,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 5,
						"lat": 41.872255,
						"lon": -87.629301,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 6,
						"lat": 41.872293,
						"lon": -87.629098,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 7,
						"lat": 41.87263,
						"lon": -87.629078,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 8,
						"lat": 41.872704999999,
						"lon": -87.629079999998,
						"typ": "S",
						"stpid": "1875",
						"stpnm": "Dearborn & Polk",
						"pdist": 1259.0
					},
					{
						"seq": 9,
						"lat": 41.874787,
						"lon": -87.629154,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 10,
						"lat": 41.874857999999,
						"lon": -87.629155999998,
						"typ": "S",
						"stpid": "1876",
						"stpnm": "Dearborn & Harrison",
						"pdist": 2045.0
					},
					{
						"seq": 11,
						"lat": 41.875955,
						"lon": -87.629182,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 12,
						"lat": 41.876090000001,
						"lon": -87.629182000001,
						"typ": "S",
						"stpid": "1877",
						"stpnm": "Dearborn & Congress",
						"pdist": 2494.0
					},
					{
						"seq": 13,
						"lat": 41.877954,
						"lon": -87.629221,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 14,
						"lat": 41.878017999999,
						"lon": -87.629222999998,
						"typ": "S",
						"stpid": "14508",
						"stpnm": "Dearborn & Jackson",
						"pdist": 3197.0
					},
					{
						"seq": 15,
						"lat": 41.879771,
						"lon": -87.629292,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 16,
						"lat": 41.879886,
						"lon": -87.629297000001,
						"typ": "S",
						"stpid": "1880",
						"stpnm": "Dearborn & Adams",
						"pdist": 3879.0
					},
					{
						"seq": 17,
						"lat": 41.880983,
						"lon": -87.62931,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 18,
						"lat": 41.881117999999,
						"lon": -87.629312,
						"typ": "S",
						"stpid": "1881",
						"stpnm": "Dearborn & Monroe",
						"pdist": 4328.0
					},
					{
						"seq": 19,
						"lat": 41.882324,
						"lon": -87.629338,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 20,
						"lat": 41.882400999999,
						"lon": -87.629336999999,
						"typ": "S",
						"stpid": "1882",
						"stpnm": "Dearborn & Madison",
						"pdist": 4796.0
					},
					{
						"seq": 21,
						"lat": 41.884703,
						"lon": -87.629404,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 22,
						"lat": 41.884798000001,
						"lon": -87.629408,
						"typ": "S",
						"stpid": "1884",
						"stpnm": "Dearborn & Randolph",
						"pdist": 5671.0
					},
					{
						"seq": 23,
						"lat": 41.886223,
						"lon": -87.629449,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 24,
						"lat": 41.886351999999,
						"lon": -87.629452999999,
						"typ": "S",
						"stpid": "1885",
						"stpnm": "Dearborn Between Lake & Wacker (MB)",
						"pdist": 6238.0
					},
					{
						"seq": 25,
						"lat": 41.888216,
						"lon": -87.629469,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 26,
						"lat": 41.888308999999,
						"lon": -87.62947,
						"typ": "S",
						"stpid": "1887",
						"stpnm": "Dearborn & Marina City",
						"pdist": 6952.0
					},
					{
						"seq": 27,
						"lat": 41.889844,
						"lon": -87.629526,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 28,
						"lat": 41.889911999999,
						"lon": -87.629528,
						"typ": "S",
						"stpid": "15399",
						"stpnm": "Dearborn & Hubbard",
						"pdist": 7537.0
					},
					{
						"seq": 29,
						"lat": 41.891885,
						"lon": -87.629595,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 30,
						"lat": 41.89197,
						"lon": -87.62967,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 31,
						"lat": 41.891971000001,
						"lon": -87.629599000002,
						"typ": "S",
						"stpid": "14767",
						"stpnm": "Dearborn & Grand",
						"pdist": 8313.0
					},
					{
						"seq": 32,
						"lat": 41.89197,
						"lon": -87.62967,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 33,
						"lat": 41.892948,
						"lon": -87.629695,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 34,
						"lat": 41.893108,
						"lon": -87.629610999999,
						"typ": "S",
						"stpid": "1891",
						"stpnm": "Dearborn & Ontario",
						"pdist": 8752.0
					},
					{
						"seq": 35,
						"lat": 41.89311,
						"lon": -87.6297,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 36,
						"lat": 41.89472,
						"lon": -87.62974,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 37,
						"lat": 41.894719999999,
						"lon": -87.629655000001,
						"typ": "S",
						"stpid": "1892",
						"stpnm": "Dearborn & Huron",
						"pdist": 9385.0
					},
					{
						"seq": 38,
						"lat": 41.89472,
						"lon": -87.62974,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 39,
						"lat": 41.8968,
						"lon": -87.6298,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 40,
						"lat": 41.8968,
						"lon": -87.629704999999,
						"typ": "S",
						"stpid": "18447",
						"stpnm": "Dearborn & Chicago",
						"pdist": 10193.0
					},
					{
						"seq": 41,
						"lat": 41.8968,
						"lon": -87.6298,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 42,
						"lat": 41.898865,
						"lon": -87.629835,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 43,
						"lat": 41.898982,
						"lon": -87.629811,
						"typ": "S",
						"stpid": "1895",
						"stpnm": "Dearborn & Delaware",
						"pdist": 11017.0
					},
					{
						"seq": 44,
						"lat": 41.89898,
						"lon": -87.62983,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 45,
						"lat": 41.89981,
						"lon": -87.62987,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 46,
						"lat": 41.89979,
						"lon": -87.63097,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 47,
						"lat": 41.899893,
						"lon": -87.630967,
						"typ": "S",
						"stpid": "18412",
						"stpnm": "Walton & Dearborn",
						"pdist": 11663.0
					},
					{
						"seq": 48,
						"lat": 41.89979,
						"lon": -87.63097,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 49,
						"lat": 41.89979,
						"lon": -87.63133,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 50,
						"lat": 41.90045,
						"lon": -87.63135,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 51,
						"lat": 41.900455000001,
						"lon": -87.631294000002,
						"typ": "S",
						"stpid": "1897",
						"stpnm": "Clark & Oak",
						"pdist": 12055.0
					},
					{
						"seq": 52,
						"lat": 41.90045,
						"lon": -87.63135,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 53,
						"lat": 41.90171,
						"lon": -87.631294,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 54,
						"lat": 41.901775,
						"lon": -87.631279000002,
						"typ": "S",
						"stpid": "1898",
						"stpnm": "Clark & Maple",
						"pdist": 12552.0
					},
					{
						"seq": 55,
						"lat": 41.903618,
						"lon": -87.631294,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 56,
						"lat": 41.903763000001,
						"lon": -87.631255999998,
						"typ": "S",
						"stpid": "1899",
						"stpnm": "Clark & Division (Red Line)",
						"pdist": 13281.0
					},
					{
						"seq": 57,
						"lat": 41.90385,
						"lon": -87.631409,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 58,
						"lat": 41.90564,
						"lon": -87.631409,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 59,
						"lat": 41.905669999999,
						"lon": -87.631462000001,
						"typ": "S",
						"stpid": "1900",
						"stpnm": "Clark & Goethe",
						"pdist": 14007.0
					},
					{
						"seq": 60,
						"lat": 41.907593,
						"lon": -87.631454,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 61,
						"lat": 41.907742000001,
						"lon": -87.631432000002,
						"typ": "S",
						"stpid": "1901",
						"stpnm": "Clark & Schiller",
						"pdist": 14770.0
					},
					{
						"seq": 62,
						"lat": 41.908619,
						"lon": -87.631493,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 63,
						"lat": 41.909252,
						"lon": -87.631462,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 64,
						"lat": 41.909373999999,
						"lon": -87.631455,
						"typ": "S",
						"stpid": "1902",
						"stpnm": "Clark & Burton",
						"pdist": 15365.0
					},
					{
						"seq": 65,
						"lat": 41.909336,
						"lon": -87.631562,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 66,
						"lat": 41.911255,
						"lon": -87.631609,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 67,
						"lat": 41.911424,
						"lon": -87.631695,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 68,
						"lat": 41.911512000001,
						"lon": -87.631646999999,
						"typ": "S",
						"stpid": "15417",
						"stpnm": "Clark & North Avenue",
						"pdist": 16186.0
					},
					{
						"seq": 69,
						"lat": 41.913384,
						"lon": -87.632913,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 70,
						"lat": 41.913547,
						"lon": -87.633029999999,
						"typ": "S",
						"stpid": "1451",
						"stpnm": "Clark & Lasalle",
						"pdist": 17014.0
					},
					{
						"seq": 71,
						"lat": 41.915438,
						"lon": -87.634143,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 72,
						"lat": 41.915564999999,
						"lon": -87.634193000002,
						"typ": "S",
						"stpid": "1905",
						"stpnm": "Clark & Lincoln",
						"pdist": 17815.0
					},
					{
						"seq": 73,
						"lat": 41.916552,
						"lon": -87.634827,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 74,
						"lat": 41.916687,
						"lon": -87.634904999998,
						"typ": "S",
						"stpid": "1906",
						"stpnm": "Clark & Wisconsin",
						"pdist": 18271.0
					},
					{
						"seq": 75,
						"lat": 41.918243,
						"lon": -87.63586,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 76,
						"lat": 41.918355,
						"lon": -87.636176999999,
						"typ": "S",
						"stpid": "1907",
						"stpnm": "Clark & Armitage",
						"pdist": 18995.0
					},
					{
						"seq": 77,
						"lat": 41.91915,
						"lon": -87.636797,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 78,
						"lat": 41.919905,
						"lon": -87.637258,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 79,
						"lat": 41.920047999999,
						"lon": -87.637304999999,
						"typ": "S",
						"stpid": "1908",
						"stpnm": "Clark & Dickens",
						"pdist": 19686.0
					},
					{
						"seq": 80,
						"lat": 41.920302,
						"lon": -87.637512,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 81,
						"lat": 41.921828,
						"lon": -87.638402,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 82,
						"lat": 41.921875,
						"lon": -87.638402000001,
						"typ": "S",
						"stpid": "1909",
						"stpnm": "Clark & Webster",
						"pdist": 20418.0
					},
					{
						"seq": 83,
						"lat": 41.922122,
						"lon": -87.638608,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 84,
						"lat": 41.922822,
						"lon": -87.639038,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 85,
						"lat": 41.923632,
						"lon": -87.639435,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 86,
						"lat": 41.923648,
						"lon": -87.639451999999,
						"typ": "S",
						"stpid": "1910",
						"stpnm": "Clark & Belden",
						"pdist": 21133.0
					},
					{
						"seq": 87,
						"lat": 41.925283,
						"lon": -87.640428,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 88,
						"lat": 41.925437000001,
						"lon": -87.640516999999,
						"typ": "S",
						"stpid": "1911",
						"stpnm": "Clark & Fullerton",
						"pdist": 21845.0
					},
					{
						"seq": 89,
						"lat": 41.926856,
						"lon": -87.641209,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 90,
						"lat": 41.927032999999,
						"lon": -87.641295,
						"typ": "S",
						"stpid": "17266",
						"stpnm": "Clark & Arlington",
						"pdist": 22466.0
					},
					{
						"seq": 91,
						"lat": 41.928494,
						"lon": -87.642143,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 92,
						"lat": 41.928542999999,
						"lon": -87.642408,
						"typ": "S",
						"stpid": "1913",
						"stpnm": "Clark & Deming",
						"pdist": 23090.0
					},
					{
						"seq": 93,
						"lat": 41.929559,
						"lon": -87.64276,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 94,
						"lat": 41.930016,
						"lon": -87.643429,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 95,
						"lat": 41.930185,
						"lon": -87.643572,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 96,
						"lat": 41.930787,
						"lon": -87.643899,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 97,
						"lat": 41.930824999999,
						"lon": -87.643918,
						"typ": "S",
						"stpid": "1915",
						"stpnm": "Clark & Drummond",
						"pdist": 24042.0
					},
					{
						"seq": 98,
						"lat": 41.931698,
						"lon": -87.644456,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 99,
						"lat": 41.932139,
						"lon": -87.644697,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 100,
						"lat": 41.932825,
						"lon": -87.644908,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 101,
						"lat": 41.933097,
						"lon": -87.645142,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 102,
						"lat": 41.933128000001,
						"lon": -87.645172999999,
						"typ": "S",
						"stpid": "1917",
						"stpnm": "Clark & Diversey",
						"pdist": 24961.0
					},
					{
						"seq": 103,
						"lat": 41.933263,
						"lon": -87.645332,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 104,
						"lat": 41.934535,
						"lon": -87.646333,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 105,
						"lat": 41.934583000001,
						"lon": -87.646397000001,
						"typ": "S",
						"stpid": "1918",
						"stpnm": "Clark & Surf",
						"pdist": 25586.0
					},
					{
						"seq": 106,
						"lat": 41.934822,
						"lon": -87.64635,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 107,
						"lat": 41.934965,
						"lon": -87.646508,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 108,
						"lat": 41.936618,
						"lon": -87.64778,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 109,
						"lat": 41.936690000001,
						"lon": -87.647843,
						"typ": "S",
						"stpid": "14919",
						"stpnm": "Clark & Wellington",
						"pdist": 26467.0
					},
					{
						"seq": 110,
						"lat": 41.937072,
						"lon": -87.648257,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 111,
						"lat": 41.937787,
						"lon": -87.648828,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 112,
						"lat": 41.937897,
						"lon": -87.648972,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 113,
						"lat": 41.93858,
						"lon": -87.649465,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 114,
						"lat": 41.93874,
						"lon": -87.649608,
						"typ": "S",
						"stpid": "14437",
						"stpnm": "Clark & Barry/Halsted",
						"pdist": 27358.0
					},
					{
						"seq": 115,
						"lat": 41.939725,
						"lon": -87.650355,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 116,
						"lat": 41.939757,
						"lon": -87.650497999998,
						"typ": "S",
						"stpid": "1921",
						"stpnm": "Clark & Belmont",
						"pdist": 27814.0
					},
					{
						"seq": 117,
						"lat": 41.940162,
						"lon": -87.650927,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 118,
						"lat": 41.941473,
						"lon": -87.651945,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 119,
						"lat": 41.941616999999,
						"lon": -87.652008,
						"typ": "S",
						"stpid": "1922",
						"stpnm": "Clark & School/Aldine",
						"pdist": 28611.0
					},
					{
						"seq": 120,
						"lat": 41.941707,
						"lon": -87.652023,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 121,
						"lat": 41.943658,
						"lon": -87.653613,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 122,
						"lat": 41.943711000001,
						"lon": -87.653655,
						"typ": "S",
						"stpid": "18083",
						"stpnm": "Clark & Roscoe",
						"pdist": 29498.0
					},
					{
						"seq": 123,
						"lat": 41.944825,
						"lon": -87.654499,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 124,
						"lat": 41.944915,
						"lon": -87.654502999998,
						"typ": "S",
						"stpid": "14434",
						"stpnm": "Clark & Newport/Sheffield",
						"pdist": 29997.0
					},
					{
						"seq": 125,
						"lat": 41.947005,
						"lon": -87.6563,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 126,
						"lat": 41.947108000001,
						"lon": -87.656363000001,
						"typ": "S",
						"stpid": "1926",
						"stpnm": "Clark & Addison",
						"pdist": 30943.0
					},
					{
						"seq": 127,
						"lat": 41.94857,
						"lon": -87.657555,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 128,
						"lat": 41.949118,
						"lon": -87.657953,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 129,
						"lat": 41.94923,
						"lon": -87.658048,
						"typ": "S",
						"stpid": "18033",
						"stpnm": "Clark & Waveland",
						"pdist": 31844.0
					},
					{
						"seq": 130,
						"lat": 41.9508,
						"lon": -87.65932,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 131,
						"lat": 41.950907000001,
						"lon": -87.659414999998,
						"typ": "S",
						"stpid": "14438",
						"stpnm": "Clark & Grace",
						"pdist": 32562.0
					},
					{
						"seq": 132,
						"lat": 41.952635,
						"lon": -87.660814,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 133,
						"lat": 41.952758000001,
						"lon": -87.660893000001,
						"typ": "S",
						"stpid": "1929",
						"stpnm": "Clark & Byron",
						"pdist": 33347.0
					},
					{
						"seq": 134,
						"lat": 41.953283,
						"lon": -87.661353,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 135,
						"lat": 41.954555,
						"lon": -87.662277,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 136,
						"lat": 41.954672999999,
						"lon": -87.662340000001,
						"typ": "S",
						"stpid": "6281",
						"stpnm": "Clark & Irving Park",
						"pdist": 34148.0
					},
					{
						"seq": 137,
						"lat": 41.954825,
						"lon": -87.662483,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 138,
						"lat": 41.956407,
						"lon": -87.663437,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 139,
						"lat": 41.956565,
						"lon": -87.663515,
						"typ": "S",
						"stpid": "1931",
						"stpnm": "Clark & Belle Plaine",
						"pdist": 34908.0
					},
					{
						"seq": 140,
						"lat": 41.957018,
						"lon": -87.66385,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 141,
						"lat": 41.957337,
						"lon": -87.663993,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 142,
						"lat": 41.957431999999,
						"lon": -87.664057000001,
						"typ": "S",
						"stpid": "15541",
						"stpnm": "Clark & Southport",
						"pdist": 35261.0
					},
					{
						"seq": 143,
						"lat": 41.958043,
						"lon": -87.664438,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 144,
						"lat": 41.959197,
						"lon": -87.664978,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 145,
						"lat": 41.95972,
						"lon": -87.665153,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 146,
						"lat": 41.959777000001,
						"lon": -87.665152999998,
						"typ": "S",
						"stpid": "1933",
						"stpnm": "Clark & Cullom",
						"pdist": 36169.0
					},
					{
						"seq": 147,
						"lat": 41.959855,
						"lon": -87.665263,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 148,
						"lat": 41.961525,
						"lon": -87.6659,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 149,
						"lat": 41.961843,
						"lon": -87.665963,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 150,
						"lat": 41.961946999999,
						"lon": -87.665995,
						"typ": "S",
						"stpid": "15518",
						"stpnm": "Clark & Montrose",
						"pdist": 36998.0
					},
					{
						"seq": 151,
						"lat": 41.963178,
						"lon": -87.66625,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 152,
						"lat": 41.963353000001,
						"lon": -87.666297000001,
						"typ": "S",
						"stpid": "1935",
						"stpnm": "Clark & Sunnyside",
						"pdist": 37518.0
					},
					{
						"seq": 153,
						"lat": 41.963678,
						"lon": -87.666408,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 154,
						"lat": 41.965077,
						"lon": -87.666647,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 155,
						"lat": 41.965187999999,
						"lon": -87.666662999999,
						"typ": "S",
						"stpid": "1936",
						"stpnm": "Clark & Wilson",
						"pdist": 38203.0
					},
					{
						"seq": 156,
						"lat": 41.965903,
						"lon": -87.666885,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 157,
						"lat": 41.966928,
						"lon": -87.66706,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 158,
						"lat": 41.966985,
						"lon": -87.66706,
						"typ": "S",
						"stpid": "1937",
						"stpnm": "Clark & Leland",
						"pdist": 38868.0
					},
					{
						"seq": 159,
						"lat": 41.967485,
						"lon": -87.667218,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 160,
						"lat": 41.968573,
						"lon": -87.667442,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 161,
						"lat": 41.969115,
						"lon": -87.66749,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 162,
						"lat": 41.969129999999,
						"lon": -87.667489999999,
						"typ": "S",
						"stpid": "17395",
						"stpnm": "Clark & Lawrence",
						"pdist": 39658.0
					},
					{
						"seq": 163,
						"lat": 41.969288,
						"lon": -87.667568,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 164,
						"lat": 41.971625,
						"lon": -87.667775,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 165,
						"lat": 41.971722,
						"lon": -87.667807,
						"typ": "S",
						"stpid": "1939",
						"stpnm": "Clark & Ainslie",
						"pdist": 40607.0
					},
					{
						"seq": 166,
						"lat": 41.973517,
						"lon": -87.668093,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 167,
						"lat": 41.973683000001,
						"lon": -87.668109999999,
						"typ": "S",
						"stpid": "14789",
						"stpnm": "Clark & Winnemac",
						"pdist": 41323.0
					},
					{
						"seq": 168,
						"lat": 41.973843,
						"lon": -87.668205,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 169,
						"lat": 41.975988,
						"lon": -87.668412,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 170,
						"lat": 41.975997,
						"lon": -87.66838,
						"typ": "S",
						"stpid": "1942",
						"stpnm": "Clark & Foster",
						"pdist": 42180.0
					},
					{
						"seq": 171,
						"lat": 41.977317,
						"lon": -87.66838,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 172,
						"lat": 41.977762,
						"lon": -87.668332,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 173,
						"lat": 41.977848,
						"lon": -87.668332,
						"typ": "S",
						"stpid": "1943",
						"stpnm": "Clark & Berwyn",
						"pdist": 42854.0
					},
					{
						"seq": 174,
						"lat": 41.978317,
						"lon": -87.66838,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 175,
						"lat": 41.979955,
						"lon": -87.668283,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 176,
						"lat": 41.980050000001,
						"lon": -87.668283000001,
						"typ": "S",
						"stpid": "14791",
						"stpnm": "Clark & Balmoral",
						"pdist": 43644.0
					},
					{
						"seq": 177,
						"lat": 41.9802,
						"lon": -87.668363,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 178,
						"lat": 41.9814,
						"lon": -87.668427,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 179,
						"lat": 41.981497,
						"lon": -87.668426999999,
						"typ": "S",
						"stpid": "1945",
						"stpnm": "Clark & Catalpa",
						"pdist": 44181.0
					},
					{
						"seq": 180,
						"lat": 41.9816,
						"lon": -87.66838,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 181,
						"lat": 41.982783,
						"lon": -87.668602,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 182,
						"lat": 41.983595,
						"lon": -87.668682,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 183,
						"lat": 41.983658000001,
						"lon": -87.668697000001,
						"typ": "S",
						"stpid": "14792",
						"stpnm": "Clark & Bryn Mawr",
						"pdist": 44974.0
					},
					{
						"seq": 184,
						"lat": 41.985112,
						"lon": -87.669015,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 185,
						"lat": 41.985254999999,
						"lon": -87.669175000001,
						"typ": "S",
						"stpid": "1948",
						"stpnm": "Clark & Hollywood",
						"pdist": 45579.0
					},
					{
						"seq": 186,
						"lat": 41.98539,
						"lon": -87.669095,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 187,
						"lat": 41.986415,
						"lon": -87.669428,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 188,
						"lat": 41.98729,
						"lon": -87.669572,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 189,
						"lat": 41.987672,
						"lon": -87.669555,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 190,
						"lat": 41.98814,
						"lon": -87.66962,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 191,
						"lat": 41.988172000001,
						"lon": -87.669620000001,
						"typ": "S",
						"stpid": "1950",
						"stpnm": "Clark & Ardmore",
						"pdist": 46660.0
					},
					{
						"seq": 192,
						"lat": 41.988482,
						"lon": -87.669698,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 193,
						"lat": 41.98911,
						"lon": -87.66973,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 194,
						"lat": 41.989259999999,
						"lon": -87.669746999999,
						"typ": "S",
						"stpid": "1951",
						"stpnm": "Clark & Ridge",
						"pdist": 47059.0
					},
					{
						"seq": 195,
						"lat": 41.989952,
						"lon": -87.669827,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 196,
						"lat": 41.990468,
						"lon": -87.66981,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 197,
						"lat": 41.990683,
						"lon": -87.669905,
						"typ": "S",
						"stpid": "1952",
						"stpnm": "Clark & Elmdale/Peterson",
						"pdist": 47582.0
					},
					{
						"seq": 198,
						"lat": 41.990985,
						"lon": -87.669953,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 199,
						"lat": 41.992408,
						"lon": -87.669953,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 200,
						"lat": 41.992517999999,
						"lon": -87.669905000001,
						"typ": "S",
						"stpid": "1953",
						"stpnm": "Clark & Glenlake",
						"pdist": 48257.0
					},
					{
						"seq": 201,
						"lat": 41.993592,
						"lon": -87.67,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 202,
						"lat": 41.994562,
						"lon": -87.67,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 203,
						"lat": 41.994728,
						"lon": -87.670000000001,
						"typ": "S",
						"stpid": "17218",
						"stpnm": "Clark & Granville",
						"pdist": 49062.0
					},
					{
						"seq": 204,
						"lat": 41.99542,
						"lon": -87.670065,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 205,
						"lat": 41.99608,
						"lon": -87.670048,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 206,
						"lat": 41.996293,
						"lon": -87.670080000001,
						"typ": "S",
						"stpid": "1955",
						"stpnm": "Clark & Rosemont",
						"pdist": 49635.0
					},
					{
						"seq": 207,
						"lat": 41.997812,
						"lon": -87.670382,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 208,
						"lat": 41.997915,
						"lon": -87.670398000001,
						"typ": "S",
						"stpid": "1956",
						"stpnm": "Clark & Devon",
						"pdist": 50239.0
					},
					{
						"seq": 209,
						"lat": 41.99805,
						"lon": -87.67051,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 210,
						"lat": 42.000085,
						"lon": -87.671193,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 211,
						"lat": 42.000154999999,
						"lon": -87.671224999999,
						"typ": "S",
						"stpid": "1957",
						"stpnm": "Clark & Arthur",
						"pdist": 51089.0
					},
					{
						"seq": 212,
						"lat": 42.001443,
						"lon": -87.671702,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 213,
						"lat": 42.001594999999,
						"lon": -87.671717000002,
						"typ": "S",
						"stpid": "1958",
						"stpnm": "Clark & Albion",
						"pdist": 51630.0
					},
					{
						"seq": 214,
						"lat": 42.003398,
						"lon": -87.672353,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 215,
						"lat": 42.003438,
						"lon": -87.672368000002,
						"typ": "S",
						"stpid": "1959",
						"stpnm": "Clark & North Shore",
						"pdist": 52331.0
					},
					{
						"seq": 216,
						"lat": 42.003843,
						"lon": -87.672543,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 217,
						"lat": 42.005433,
						"lon": -87.673005,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 218,
						"lat": 42.005519999999,
						"lon": -87.673020000002,
						"typ": "S",
						"stpid": "14436",
						"stpnm": "Clark & Pratt",
						"pdist": 53116.0
					},
					{
						"seq": 219,
						"lat": 42.005687,
						"lon": -87.673132,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 220,
						"lat": 42.007093,
						"lon": -87.673465,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 221,
						"lat": 42.007888,
						"lon": -87.673577,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 222,
						"lat": 42.007905000001,
						"lon": -87.673576999999,
						"typ": "S",
						"stpid": "14785",
						"stpnm": "Clark & Morse",
						"pdist": 53992.0
					},
					{
						"seq": 223,
						"lat": 42.008692,
						"lon": -87.673799,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 224,
						"lat": 42.008867,
						"lon": -87.673877999999,
						"typ": "S",
						"stpid": "1963",
						"stpnm": "Clark & Lunt",
						"pdist": 54351.0
					},
					{
						"seq": 225,
						"lat": 42.01017,
						"lon": -87.674165,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 226,
						"lat": 42.010320000001,
						"lon": -87.674181999998,
						"typ": "S",
						"stpid": "17219",
						"stpnm": "Clark & Greenleaf",
						"pdist": 54890.0
					},
					{
						"seq": 227,
						"lat": 42.011448,
						"lon": -87.674403,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 228,
						"lat": 42.013015,
						"lon": -87.674578,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 229,
						"lat": 42.013102000001,
						"lon": -87.67461,
						"typ": "S",
						"stpid": "14463",
						"stpnm": "Clark & Touhy",
						"pdist": 55908.0
					},
					{
						"seq": 230,
						"lat": 42.013173,
						"lon": -87.67469,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 231,
						"lat": 42.013452,
						"lon": -87.674737,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 232,
						"lat": 42.013586999999,
						"lon": -87.674768,
						"typ": "S",
						"stpid": "1967",
						"stpnm": "Clark & Chase",
						"pdist": 56095.0
					},
					{
						"seq": 233,
						"lat": 42.014962,
						"lon": -87.67504,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 234,
						"lat": 42.01574,
						"lon": -87.675087,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 235,
						"lat": 42.015820000001,
						"lon": -87.675117999998,
						"typ": "S",
						"stpid": "1968",
						"stpnm": "Clark & Jarvis",
						"pdist": 56919.0
					},
					{
						"seq": 236,
						"lat": 42.015892,
						"lon": -87.67515,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 237,
						"lat": 42.016027,
						"lon": -87.675087,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 238,
						"lat": 42.016598,
						"lon": -87.673895,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 239,
						"lat": 42.016638,
						"lon": -87.673815000001,
						"typ": "S",
						"stpid": "15452",
						"stpnm": "Rogers & Hermitage",
						"pdist": 57406.0
					},
					{
						"seq": 240,
						"lat": 42.016693,
						"lon": -87.673927,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 241,
						"lat": 42.017043,
						"lon": -87.67318,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 242,
						"lat": 42.017172,
						"lon": -87.673005,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 243,
						"lat": 42.017345,
						"lon": -87.672957,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 244,
						"lat": 42.018387,
						"lon": -87.672957,
						"typ": "W",
						"pdist": 0.0
					},
					{
						"seq": 245,
						"lat": 42.018427,
						"lon": -87.672956999998,
						"typ": "W",
						"pdist": 0.0
					}
				]
			}
		]
	}
}
'''

patternResponse = json.loads(cccc)
indexofbustoNorthbound = [i for i in range(len(patternResponse['bustime-response']['ptr'])) if patternResponse['bustime-response']['ptr'][i]['rtdir'] == 'Northbound']
patternLength = [patternResponse['bustime-response']['ptr'][indexofbustoNorthbound[l]]['ln'] for l in range(len(indexofbustoNorthbound))]
pidValues = [patternResponse['bustime-response']['ptr'][indexofbustoNorthbound[l]]['pid'] for l in range(len(indexofbustoNorthbound))]
getsequencePatternLat = [[patternResponse['bustime-response']['ptr'][indexofbustoNorthbound[k]]['pt'][j]['lat'] for j in range(len(patternResponse['bustime-response']['ptr'][indexofbustoNorthbound[k]]['pt']))] for k in range(len(indexofbustoNorthbound))]
getsequencePatternLon = []
print(getsequencePatternLat)
