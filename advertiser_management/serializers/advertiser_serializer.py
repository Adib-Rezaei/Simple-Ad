from django.contrib.auth.hashers import check_password, make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_403_FORBIDDEN
from advertiser_management.models import Advertiser
from advertiser_management.serializers.ad_serializer import AdSerializer

# POST
class AdvertiserLoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=100)


    def validate(self, attrs):
        name = attrs.get('name', None)
        user = get_object_or_404(Advertiser.objects.all(), username=name)

        if not check_password(attrs['password'], user.password):
            raise ValidationError(
                'رمز عبور اشتباه است!', code=HTTP_403_FORBIDDEN
            )

        
        attrs['user'] = user
        return attrs


#POST
class AdvertiserSignupSerializer(serializers.ModelSerializer):

    def validate_password(self, password):
        return make_password(password)

    def validate(self, attrs):
        attrs['username'] = attrs['name']
        return attrs

    class Meta:
        model = Advertiser
        fields = ['name', 'password']


# GET
class AdvertiserProfileSerializer(serializers.ModelSerializer):
    ads = AdSerializer(many=True)

    class Meta:
        model = Advertiser
        fields = ['id', 'name', 'ads']