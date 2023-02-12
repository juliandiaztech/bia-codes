from rest_framework.decorators import api_view
from django.http import HttpResponse
import json 
import pandas as pd
import requests

URL = "https://api.postcodes.io/postcodes"



@api_view(['POST'])
def request_postcodes(request):
    # data = [-2.222254, 53.533446]
    print(request)
    r = requests.get(URL, params={"lon": -2.222254, "lat": 53.533446})

    if r.status_code == 200:
        r = r.json()
        r = r["result"][0]["postcode"]
        print(r)

    return HttpResponse(json.dumps("bien"), content_type='application/json')


