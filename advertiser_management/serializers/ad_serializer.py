
from rest_framework import serializers
from advertiser_management.models import Ad

class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ['id', 'created', 'title', 'img_url', 'link', 'advertiser']
        extra_kwargs = {
            'created': {
                'read_only': True
            }
        }