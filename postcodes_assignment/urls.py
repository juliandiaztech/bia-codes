from django.urls import path
from .api import request_postcodes

urlpatterns = [
        path('postcodes', request_postcodes, name='request_postcodes'),

]