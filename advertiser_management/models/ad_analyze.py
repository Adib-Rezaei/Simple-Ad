from django.db import models


DURATION_TYPE_HOURLY = 'HOURLY'
DURATION_TYPE_DAILY = 'DAILY'
DURATION_TYPES = (
        (DURATION_TYPE_HOURLY, 'ساعتی'),
        (DURATION_TYPE_DAILY, 'روزانه'),
    )

class AdAnalyze(models.Model):

    duration_type = models.CharField(
        max_length=50,
        choices=DURATION_TYPES,
        verbose_name='تایپ زمانی'
    )

    from_date = models.DateTimeField(
        verbose_name='از تاریخ'    
    )

    ad = models.ForeignKey(
        to='advertiser_management.ad',
        on_delete=models.CASCADE,
        related_name='analyzes',
        verbose_name='تبلیغ'
    )

    total_clicks = models.PositiveIntegerField(
        verbose_name='مجموع تعداد کلیک ها'
    )

    total_views = models.PositiveIntegerField(
        verbose_name='مجموع تعداد نمایش ها'
    )

    class Meta:
        verbose_name = 'آنالیز تبلیغ'
        verbose_name_plural = 'آنالیز تبلیغات'