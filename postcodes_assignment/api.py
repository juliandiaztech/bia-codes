from rest_framework.decorators import api_view
from django.http import HttpResponse
import json 
import pandas as pd
import requests

URL = "https://api.postcodes.io/postcodes"

# URL = "https://api.postcodes.io/postcodes?filter=postcode,longitude,latitude"

# json = {
#   "geolocations" : [{
#     "longitude":  -1.760,
#     "latitude": 55.37,
#     "widesearch": True,
#     "limit": 10
#   }, {
#     "longitude": -0.3793,
#     "latitude": 53.5517,
#     "radius": 2000,
#     "limit": 100
#   },
#   {
#     "longitude": -1.545,
#     "latitude": 52.39,
#     "radius": 2000,
#     "limit": 100
#   },
#   {
#     "longitude": -2.656,
#     "latitude": 51.41,
#     "radius": 2000,
#     "limit": 100
#   },
#   {
#     "longitude": -6.219,
#     "latitude": 49.95,
#     "limit": 10,
#     "radius": 2000
#   }]
# }


# @api_view(['POST'])
# def request_postcodes(request):
#     # data = [-2.222254, 53.533446]
#     print(request)
#     r = requests.post(URL, json=json)

#     if r.status_code == 200:
#         r = r.json()
#         # print(r)
#         r = r["result"]
#         print(r)

#         return HttpResponse(json.dumps("bien"), content_type='application/json')

@api_view(['POST'])
def request_postcodes_get_nearest(request):
    lon = request.data["lon"]
    lat = request.data["lat"]
    r = requests.get(URL, params={"lon": lon, "lat": lat})

    if r.status_code == 200:
        r = r.json()
        r = r["result"][0]["postcode"]

        return HttpResponse(json.dumps(r), content_type='application/json')


