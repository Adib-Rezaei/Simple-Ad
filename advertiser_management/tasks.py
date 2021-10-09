from celery import shared_task
from django.db.models.aggregates import Sum
from django.db.models.functions import Coalesce
from django.db.models.query_utils import Q
from django.utils import timezone

from advertiser_management.models import Ad
from advertiser_management.models.ad_analyze import DURATION_TYPE_DAILY, DURATION_TYPE_HOURLY, AdAnalyze



def annotate_total_events_hourly(query, hours):
    return query.annotate(
        total_clicks=Coalesce(
            Sum(
                'clicks',
                filter=Q(clicks__created__gt=timezone.now() - timezone.timedelta(hours=hours))
            ),
            0
        ),
        total_views=Coalesce(
            Sum(
                'views',
                filter=Q(views__created__gt=timezone.now() - timezone.timedelta(hours=hours))
            ),
            0
        )
    )

    

def annotate_total_events_daily(query, days):
    return query.annotate(
        total_clicks=Coalesce(
            Sum(
                'adanalyse__total_clicks',
                filter=Q(adanalyse_from_date__gt=timezone.now() - timezone.timedelta(days=days))
            ),
            0
        ),
        total_views=Coalesce(
            Sum(
                'adanalyse__total_views',
                filter=Q(adanalyse_from_date__gt=timezone.now() - timezone.timedelta(days=days))
            ),
            0
        )
    )

@shared_task
def hourly_report():
    query = annotate_total_events_hourly(Ad.objects.all(), 1)

    for ad in query:
        AdAnalyze.objects.create(ad=ad, from_date=timezone.now(),
         total_clicks=ad.total_clicks, total_views=ad.total_views,
         duration_type=DURATION_TYPE_HOURLY)

@shared_task
def daily_report():
    query = annotate_total_events_daily(Ad.objects.all(), 1)

    for ad in query:
        AdAnalyze.objects.create(ad=ad, from_date=timezone.now(),
         total_clicks=ad.total_clicks, total_views=ad.total_views,
         duration_type=DURATION_TYPE_DAILY)


