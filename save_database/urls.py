# from rest_framework import routers
# from .api import view_csv

# router = routers.DefaultRouter()

# router.register('api/save_codes', view_csv, 'save_codes')
# urlpatterns = router.urls


from django.urls import path
from .api import view_csv, update_postcode

urlpatterns = [
        path('file-csv', view_csv, name='view_csv'),
        path('update-codes', update_postcode, name='update_postcode'),

]