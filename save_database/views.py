from django.shortcuts import render
import requests
import pandas as pd
import scipy.stats as stats
from .models import PostCodes
from .serializers import PostCodesSerializer

def read_csv(file_csv):
    df = pd.read_csv(file_csv, header=None, names=["latitude", "longitude"], skiprows=1)
    return df

def df_transform_df_to_dict(fk, df_csv):
    df_csv=df_csv.assign(document_id=fk)
    df_raw = df_csv.to_dict('records')

    return df_raw


def clean_data_delete_duplicates(df_raw, fk):

    df_clean = df_raw.replace(r"^ +| +$", r"", regex=True)
    df_clean = df_clean.drop_duplicates()
    df_clean= df_clean.assign(document_id=fk)
    df_clean = df_clean.to_dict('records')
    # Encontramos el Q1, Q3, y el rango intercuartílico para cada columna
    Q1 = df_clean.quantile(q=.25)
    Q3 = df_clean.quantile(q=.75)
    IQR = df_clean.apply(stats.iqr)
    # Solo mantenemos filas que esten dentro de 1.5*IQR de Q1 y Q3
    df_clean = df_clean[~((df_clean < (Q1-1.5*IQR)) | (df_clean > (Q3+1.5*IQR))).any(axis=1)]

    return df_clean


def request_for_obtain_postcode_nearest(lon, lat):
    URL = "http://127.0.0.1:8000/postcodes_get_nearest"

    json_data = {'lon': lon, 'lat': lat}
    print(json_data)
    request_postcode = requests.post(URL, data=json_data)
    request_postcode = request_postcode.json()

    return request_postcode


def update_postcode_on_database(id, lon, lat, postcode):
    URL = "http://127.0.0.1:8000/update-codes"
    json_for_update_postcode = {'id': id, 'longitude':  lon, 'latitude': lat, 'postcode': postcode}
    response_update_postcode = requests.put(URL, json=json_for_update_postcode)

    return response_update_postcode


# def get_all_register():
#     queryset = PostCodes.objects.all()
#     code_serializer = PostCodesSerializer(queryset, many=True)
#     code_serializer = code_serializer.data
#     return code_serializer


def updated_outlier(df_raw, data_clean):
    df=df_raw.join(data_clean, lsuffix="_left", rsuffix="_right", how='outer')

    # Filtro los outliers
    df = df[df.lat_right.isnull()]
    # Elimino las columnas innecesarias
    df = df.drop(['lat_right','lon_right'], axis=1)
    # renombro las columnas
    df.columns= ['latitude','longitude']
    # Adiciono la columna "postcode" 
    df_data=df.assign(postcode='Fuera de UK')
    return df_data
