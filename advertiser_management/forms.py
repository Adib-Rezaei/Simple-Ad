from django.forms.models import ModelForm
from advertiser_management.models import Ad


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['advertiser', 'title', 'img_url', 'link']