from rest_framework import views
from rest_framework.response import Response

from advertiser_management.annotations import annotate_ads_report
from advertiser_management.models.ad import Ad
from advertiser_management.serializers.ad_report_serializer import AdReportSerializer


class AdReportView(views.APIView):
    queryset = Ad.objects.all()
    serializer_class = AdReportSerializer

    def get(self, request, hour):
        query = annotate_ads_report(self.queryset, int(hour))
        fields = ['id','title', 'advertiser', 'average_delay', 'total_rate', 'total_hour_events']
        serializer = self.serializer_class(data=list(query.values(*fields)), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.validated_data)