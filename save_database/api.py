from .models import PostCodes
from .serializers import PostCodesSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json 
import pandas as pd


@api_view(['GET', 'POST'])
def view_csv(request):
    if request.method == 'GET':
        queryset = PostCodes.objects.all()
        code_serializer = PostCodesSerializer(queryset, many=True)
        code_serializer = code_serializer.data
        return HttpResponse(json.dumps(code_serializer), content_type='application/json')
    elif request.method == 'POST':
        csv = request.FILES["file"]
        df = pd.read_csv(csv, header=None, names=["latitude", "longitude"], skiprows=1)
        df = df.replace(r"^ +| +$", r"", regex=True)
        df = df.drop_duplicates()
        df = df.to_dict('records')
        post_codes_serializer = PostCodesSerializer(data=df, many=True)
        if post_codes_serializer.is_valid():
            post_codes_serializer.save()
        else: 
            print(post_codes_serializer.errors)
        return HttpResponse(json.dumps("recibido"), content_type='application/json')


@api_view(['PUT'])
def update_postcode(request, pk=1010887):
        postcodes = PostCodes.objects.filter(id = pk).first()
        print("o")
        print(postcodes)
        print("o")
