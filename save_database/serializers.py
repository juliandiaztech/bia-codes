from rest_framework import serializers
from .models import PostCodes

class PostCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCodes
        fields = ('id', 'longitude', 'latitude', 'postcode', 'created_at')
        read_only_fields = ('created_at', )

    def update(self, instance, validated_data):
        print("dd")
        print(validated_data)

