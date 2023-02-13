from .models import PostCodes, MetadataFiles
from .serializers import PostCodesSerializer, MetadataFilesSerializer, RawDocumentRecordsSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json 
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import requests
from .views import read_csv, df_transform_df_to_dict, clean_data_delete_duplicates, request_for_obtain_postcode_nearest, updated_outlier #update_postcode_on_database, get_all_register, updated_outlier



@api_view(['GET', 'POST'])
def view_csv(request):

    # Retorna todos los registros de la base de datos - Tabla POSTCODES
    if request.method == 'GET':
        queryset = PostCodes.objects.all()
        code_serializer = PostCodesSerializer(queryset, many=True)
        code_serializer = code_serializer.data
        return HttpResponse(json.dumps(code_serializer), content_type='application/json')

    
    # Endpoint para recibir el archivo csv y ser puerta de entrada de la api
    elif request.method == 'POST':
        file_csv = request.FILES["file"] # 

        df_csv = read_csv(file_csv) #funcion que lee y crea un dataframe
        number_of_records = len(df_csv)

        data_Metadata = {"name_document": "codes", "number_of_records": number_of_records}
        metadata_serializer = MetadataFilesSerializer(data=data_Metadata)

        if metadata_serializer.is_valid():
            metadata_serializer.save()
            fk = metadata_serializer.instance
            fk = int(fk.id)
            
            # Tratamiento de datos para table raw
            df_raw = df_transform_df_to_dict(fk, df_csv) # transforma el dataframe en diccionario
            rawdocument_serializer = RawDocumentRecordsSerializer(data=df_raw, many=True) 
            if rawdocument_serializer.is_valid():
                rawdocument_serializer.save()
            else: 
                print(rawdocument_serializer.errors)
            
            # Tratamiento de datos para tabla POSTCODES - con data limpia
            df_clean = clean_data_delete_duplicates(df_raw, fk) # funcion para limpiar los datos y eliminar duplicados
            post_codes_serializer = PostCodesSerializer(data=df_clean, many=True)
            if post_codes_serializer.is_valid():
                post_codes_serializer.save()
            else: 
                print(post_codes_serializer.errors)

            # Tratamiento de datos para los OUTLIER  para tabla POSTCODES - 
            data_ourlier= updated_outlier(df_raw, df_clean)
            print(data_ourlier)
            post_codes_serializer = PostCodesSerializer(data=data_ourlier, many=True)
            if post_codes_serializer.is_valid():
                post_codes_serializer.save()
            else: 
                print(post_codes_serializer.errors)

            # Request para obtener postcode de la api https://postcodes.io/

            # register = get_all_register()
            # print("luisa")
            # print(register)

            
            # postcode = request_for_obtain_postcode_nearest(lon, lat) 
 
            # # Request para actualizar postcode en la base de datos

            # re = update_postcode_on_database(id, lon, lat, postcode)



        return HttpResponse(json.dumps("recibido"), content_type='application/json')




@api_view(['PUT'])
def update_postcode(request, pk=None):
    pk = request.data
    pk = pk["id"]
    postcodes = PostCodes.objects.filter(id = pk).first()
    postcodesSerializer = PostCodesSerializer(postcodes, data=request.data)
    if postcodesSerializer.is_valid():
        postcodesSerializer.save()
        return HttpResponse(json.dumps("listones"), content_type='application/json')
