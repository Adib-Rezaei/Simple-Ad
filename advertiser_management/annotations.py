from django.db.models.aggregates import Avg, Count, Sum
from django.db.models.expressions import F, OuterRef, Subquery
from django.db.models.fields import FloatField
from django.db.models.functions import Coalesce
from django.db.models.functions.comparison import Cast
from django.db.models.query_utils import Q
from django.utils import timezone

from advertiser_management.models.event import Click, View


def annotate_hourly_ad_events(queryset, hour):
    return queryset.annotate(
        total_hour_events=Count(
            'clicks',
            filter=Q(clicks__created__time__hour__range=[hour, hour+1]),
            distinct=True
        ) + Count(
            'views',
            filter=Q(views__created__time__hour__range=[hour, hour+1]),
            distinct=True
        )
    ).order_by('-created')

def annotate_event_rate(queryset):
    queryset = queryset.annotate(total_views=Count('views', distinct=True),
                                total_clicks=Count('clicks', distinct=True))
    queryset = queryset.exclude(total_views=0).annotate(
        total_rate=Cast('total_clicks', FloatField()) / Cast('total_views', FloatField())
    )

    return queryset


def annotate_average_click_delay(queryset):
    return queryset.annotate(
        average_delay=Avg('clicks__delay')
    )


def annotate_ads_report(queryset, hour):
    return annotate_average_click_delay(
            annotate_event_rate(
                annotate_hourly_ad_events(queryset, hour)
            )
        )

# Click.objects.filter(ad__id=OuterRef('id'), created__time__hour__range=[hour, hour+1])