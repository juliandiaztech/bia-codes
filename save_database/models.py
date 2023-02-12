from django.db import models

class PostCodes(models.Model):
    longitude = models.FloatField(max_length=12)
    latitude = models.FloatField(max_length=12)
    postcode = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)