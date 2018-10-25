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

print(requests_json)

print(requests_json.keys())

print(len(requests_json['features']))

print(requests_json['features'][0].keys())

print(requests_json['features'][0]['properties'].keys())

print(requests_json['features'][0]['properties']['mag'])


