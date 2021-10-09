from django.db.models.fields import FloatField
from rest_framework import serializers

from advertiser_management.models import Ad


class AdReportSerializer(serializers.ModelSerializer):
    average_delay = serializers.DurationField(allow_null=True)
    total_rate = serializers.FloatField()
    total_hour_events = serializers.IntegerField()
    advertiser = serializers.IntegerField()

    class Meta:
        model = Ad
        fields = ['id','title', 'advertiser', 'average_delay', 'total_rate', 'total_hour_events']
