from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce


class Advertiser(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name='نام'
    )

    @property
    def total_clicks(self):
        return self.ads.aggregate(total_clicks=Coalesce(
            Sum('clicks'),
            0
        )).get('total_clicks')

    @property
    def total_views(self):
        return self.ads.aggregate(total_views=Coalesce(
            Sum('views'),
            0
        )).get('total_views')

    def __str__(self) -> str:
        return str(self.id) + ' - ' + str(self.name)

    class Meta:
        verbose_name = 'تبلیغ کننده'
        verbose_name_plural = 'تبلیغ کنندگان'