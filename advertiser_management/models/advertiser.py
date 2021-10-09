from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db.models.aggregates import Count
from django.db.models.functions import Coalesce

from advertiser_management.models.base_model import BaseHistoryModel


class Advertiser(User, BaseHistoryModel):

    name = models.CharField(
        max_length=100,
        verbose_name='نام'
    )

    @property
    def total_clicks(self):
        return self.ads.aggregate(total_clicks=Coalesce(
            Count('clicks'),
            0
        )).get('total_clicks')

    @property
    def total_views(self):
        return self.ads.aggregate(total_views=Coalesce(
            Count('views'),
            0
        )).get('total_views')

    def __str__(self) -> str:
        return str(self.id) + ' - ' + str(self.name)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.usesrname = self.name 
        super(Advertiser, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'تبلیغ کننده'
        verbose_name_plural = 'تبلیغ کنندگان'