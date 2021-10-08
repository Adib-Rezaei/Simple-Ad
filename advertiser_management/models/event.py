from django.db import models
from django.utils import timezone

from advertiser_management.models.base_model import CreateHistoryModel


class BaseEventModel(CreateHistoryModel):
    ip = models.GenericIPAddressField()

    class Meta:
        abstract = True


class Click(BaseEventModel):

    delay = models.DurationField(
        verbose_name='اختلاف زمان نمایش و کلیک',
        null=True
    )

    ad = models.ForeignKey(
        to='advertiser_management.ad',
        on_delete=models.CASCADE,
        related_name='clicks',
        verbose_name='تبلیغ'
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.delay = timezone.now() - self.ad.views.filter(ip=self.ip).order_by('-created').first().created
        super(Click, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'کلیک'
        verbose_name_plural = 'کلیک ها'


class View(BaseEventModel):

    ad = models.ForeignKey(
        to='advertiser_management.ad',
        on_delete=models.CASCADE,
        related_name='views',
        verbose_name='تبلیغ'
    )

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = 'نمایش'
        verbose_name_plural = 'نمایش ها'