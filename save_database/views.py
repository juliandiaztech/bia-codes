from django.shortcuts import render
import requests
import pandas as pd
import scipy.stats as stats
from .models import PostCodes
from .serializers import PostCodesSerializer
import json

def read_csv(file_csv):
    df = pd.read_csv(file_csv, header=None, names=["latitude", "longitude"], skiprows=1)
    return df

def df_transform_df_to_dict(fk, df_csv):
    df_csv=df_csv.assign(document_id=fk)
    df_raw = df_csv.to_dict('records')

    return df_raw


def clean_data_delete_duplicates(df_raw, fk):
    df_raw = pd.DataFrame(df_raw)
    df_clean = df_raw.replace(r"^ +| +$", r"", regex=True)
    df_clean = df_clean.drop_duplicates()
    df_clean= df_clean.assign(document_id=fk)
    # Encontramos el Q1, Q3, y el rango intercuartílico para cada columna
    Q1 = df_clean.quantile(q=.25)
    Q3 = df_clean.quantile(q=.75)
    IQR = df_clean.apply(stats.iqr)
    # Solo mantenemos filas que esten dentro de 1.5*IQR de Q1 y Q3
    df_clean = df_clean[~((df_clean < (Q1-1.5*IQR)) | (df_clean > (Q3+1.5*IQR))).any(axis=1)]
    df_clean = df_clean.to_dict('records')

    return df_clean


def request_for_obtain_postcode_nearest(lon, lat):
    URL = "http://127.0.0.1:8000/postcodes_get_nearest"

    json_data = {'lon': lon, 'lat': lat}
    request_postcode = requests.post(URL, data=json_data)

    if request_postcode.status_code ==200:
        request_postcode = request_postcode.json()
        return request_postcode
    else:
        print(request_postcode.status_code)

# update_postcode_on_database(id, lon, lat, postcode)

def update_postcode_on_database(id, lon, lat, postcode):
    URL = "http://127.0.0.1:8000/update-codes"
    json_for_update_postcode = {"id": id, "longitude":  lon, "latitude": lat, "postcode": postcode}
    print(type(json_for_update_postcode))
    response_update_postcode = requests.put(URL, data=json_for_update_postcode)

    return response_update_postcode



def updated_outlier(df_raw, data_clean):
    # Hallar las coordenadas fuera de UK para no hacer consultas inecesarias a la API
    df_raw = pd.DataFrame(df_raw)
    df_raw = df_raw.drop_duplicates()
    df=df_raw.join(data_clean, lsuffix="_left", rsuffix="_right", how='outer')
    # Filtro los outliers
    df = df[df.latitude_right.isnull()]
    # Elimino las columnas innecesarias
    df = df.drop(['latitude_right','longitude_right',  'document_id_right'], axis=1)
    # renombro las columnas
    df.columns= ['latitude','longitude', 'document_id']
    # Adiciono la columna "postcode" 
    df_data=df.assign(postcode='Fuera de UK')
    df_data = df_data.to_dict('records')
    return df_data
