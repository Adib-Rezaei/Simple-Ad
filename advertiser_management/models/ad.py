from django.db import models


class Ad(models.Model):

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

    clicks = models.PositiveIntegerField(
        default=0,
        verbose_name='تعداد کلیک'
    )

    views = models.PositiveIntegerField(
        default=0,
        verbose_name='تعداد نمایش'
    )

    advertiser = models.ForeignKey(
        to='advertiser_management.advertiser',
        on_delete=models.CASCADE,
        related_name='ads',
        verbose_name='تبلیغ کننده'
    )

    def __str__(self) -> str:
        return str(self.id) + ' - ' + str(self.title)

    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'