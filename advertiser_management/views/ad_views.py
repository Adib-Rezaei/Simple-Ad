from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from advertiser_management.models.ad import Ad
from advertiser_management.models.event import View
from advertiser_management.models.advertiser import Advertiser
from advertiser_management.serializers.ad_serializer import AdSerializer
from advertiser_management.serializers.advertiser_serializer import \
    AdvertiserProfileSerializer


class ListRetrieveCreateViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    pass


class AdvertiserViewSet(ReadOnlyModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        for advertiser in queryset:
            for ad in advertiser.ads.all():
                View.objects.create(ad=ad, ip=kwargs['ip'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AdViewSet(ListRetrieveCreateViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

