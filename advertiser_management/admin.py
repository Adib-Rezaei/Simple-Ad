from django.contrib import admin
from advertiser_management.annotations import annotate_event_rate
from advertiser_management.models.ad import Ad

from advertiser_management.models.advertiser import Advertiser
from advertiser_management.models.event import Click, View



class AdInline(admin.TabularInline):
    model = Ad
    extra = 0
    fields = ['title', 'img_url', 'link']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    fields = [
        'title',
        'img_url',
        'link',
        'advertiser',
        'is_approved'
    ]

    readonly_fields = [
        'created',
        'updated',
    ]

    list_display = [
        'id',
        'title',
        'link',
        'total_clicks',
        'total_views',
        'total_rate',
        'is_approved'
    ]

    search_fields = [ 
        'title'
    ]

    list_filter = [ 
        'is_approved'
    ]

    def total_clicks(self, obj):
        return obj.total_clicks

    total_clicks.short_description = 'مجموع کلیک ها'
    total_clicks.admin_order_field = 'total_clicks'

    def total_views(self, obj):
        return obj.total_views

    total_views.short_description = 'مجموع نمایش ها'
    total_views.admin_order_field = 'total_views'

    def total_rate(self, obj):
        return obj.total_rate

    total_rate.short_description = 'نرخ کلیک بر نمایش'
    total_rate.admin_order_field = 'total_rate'

    def get_queryset(self, request):
        return annotate_event_rate(
            super().get_queryset(request)
        )

@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name',
        'total_clicks',
        'total_views'
    ]

    readonly_fields = [ 
        'created',
        'updated'
    ]

    def total_clicks(self, obj):
        return obj.total_clicks

    total_clicks.short_description = 'مجموع کلیک ها'

    def total_views(self, obj):
        return obj.total_views

    total_views.short_description = 'مجموع نمایش ها'

    inlines =[
        AdInline
    ]

class BaseEventAdmin(admin.ModelAdmin):

    list_display = ['id', 'ip']

@admin.register(Click)
class ClickAdmin(BaseEventAdmin):
    readonly_fields = [ 
        'created',
        'ip',
        'delay',
    ]


@admin.register(View)
class ViewAdmin(BaseEventAdmin):
    readonly_fields = [ 
        'created',
        'ip',
    ]
