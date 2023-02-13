from rest_framework import serializers
from .models import PostCodes, MetadataFiles, RawDocumentRecords



class PostCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCodes
        fields = ('id', 'longitude', 'latitude', 'postcode', 'document_id', 'created_at')
        read_only_fields = ('created_at', )

    def update(self, instance, validated_data):

        instance.postcode = validated_data.get('postcode', instance.postcode)
        instance.save()
        return instance


class MetadataFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetadataFiles
        fields = ('id', 'name_document', 'number_of_records', 'created_at')
        read_only_fields = ('created_at', )

        


class RawDocumentRecordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RawDocumentRecords
        fields = ('id', 'longitude', 'latitude', 'document_id')
    