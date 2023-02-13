from django.urls import path
from .api import  request_postcodes_get_nearest

urlpatterns = [
        # path('postcodes', request_postcodes, name='request_postcodes'),
        path('postcodes_get_nearest', request_postcodes_get_nearest, name='request_postcodes_get_nearest'),

]