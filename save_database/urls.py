# from rest_framework import routers
# from .api import request_get_postcode

# router = routers.DefaultRouter()

# router.register('api/save_codes', request_get_postcode, 'save_codes')
# urlpatterns = router.urls


from django.urls import path
from .api import request_get_postcode, update_postcode

urlpatterns = [
        path('file-csv', request_get_postcode, name='request_get_postcode'),
        path('update-codes', update_postcode, name='update_postcode'),

]