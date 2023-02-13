from django.db import models


class MetadataFiles(models.Model):
    name_document = models.CharField(max_length=100)
    number_of_records = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='METADATA_FILES'



class RawDocumentRecords(models.Model):
    document_id = models.IntegerField(null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    class Meta:
        db_table='RAW_DOCUMENT_RECORDS'

class PostCodes(models.Model):
    document_id = models.IntegerField(null=True)
    longitude = models.FloatField(max_length=12)
    latitude = models.FloatField(max_length=12)
    postcode = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='POSTCODES'