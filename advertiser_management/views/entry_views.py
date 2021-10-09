from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from advertiser_management.serializers.advertiser_serializer import AdvertiserLoginSerializer, AdvertiserSignupSerializer


class AdvertiserEntryViewSet(ViewSet):

    @action(methods=['POST'], detail=False)
    def login(self, request):
        serializer = AdvertiserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'id': user.id, 'token': token.key})

    @action(methods=['POST'], detail=False)
    def signup(self, request):
        serializer = AdvertiserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'id': user.id, 'token': token.key,})

    @action(methods=['POST'], detail=False)
    def logout(self, request):
        if not hasattr(request.user.advertiser, 'auth_token'):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        request.user.advertiser.auth_token.delete()
        return Response(status=status.HTTP_200_OK)