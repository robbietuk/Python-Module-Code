"""
A script to load data about earth quakes using requests
Use Json to unpack the dictionary from text
Find the greatest magnitude earthquake
Find the location of that earthquake
Display the mag,long and lat of the earthquake
"""

import json
import requests

quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"}
                      )

requests_json = json.loads(quakes.text)

"""
print(requests_json.keys())

print(len(requests_json['features']))

print(requests_json['features'][0].keys())

print(requests_json['features'][0]['properties'].keys())

print(requests_json['features'][0]['properties']['mag'])
"""

# Get find largest mag.
quakes = requests_json['features']

largest_quake = quakes[0]
for quake in quakes:
    if largest_quake['properties']['mag'] < quake['properties']['mag']:
        largest_quake = quake

largest_mag = largest_quake['properties']['mag']
lat = largest_quake['geometry']['coordinates'][0]
long = largest_quake['geometry']['coordinates'][1]

print(' ')
print('The largest quake had a magnitude of {}'.format(largest_mag))
print('This occurred at lat: {} and long: {}'.format(lat, long))