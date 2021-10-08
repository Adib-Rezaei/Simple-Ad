from django.db import models

from advertiser_management.models.base_model import BaseHistoryModel


class Ad(BaseHistoryModel):

    title = models.CharField(
        max_length=100,
        verbose_name='عنوان'
    )

    img_url = models.URLField(
        max_length=200,
        verbose_name='آدرس تصویر'
    )

    link = models.URLField(
        max_length=200,
        verbose_name='لینک'
    )

    advertiser = models.ForeignKey(
        to='advertiser_management.advertiser',
        on_delete=models.CASCADE,
        related_name='ads',
        verbose_name='تبلیغ کننده'
    )

    is_approved = models.BooleanField(
        default=False,
        verbose_name='تاییده شده؟'
    )

    def __str__(self) -> str:
        return str(self.id) + ' - ' + str(self.title)

    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'