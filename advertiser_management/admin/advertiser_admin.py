from django.contrib import admin
from advertiser_management.models.ad import Ad

from advertiser_management.models.advertiser import Advertiser


class AdInline(admin.TabularInline):
    model = Ad
    extra = 0
    fields = ['title', 'img_url', 'link']


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):

    fields = [ 
        'name',
    ]

    list_display = [
        'id',
        'name',
        'total_clicks',
        'total_views'
    ]

    readonly_fields = [ 
        'created',
        'updated',
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