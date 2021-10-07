from django.contrib import admin
from advertiser_management.models.ad import Ad

from advertiser_management.models.advertiser import Advertiser



class AdInline(admin.TabularInline):
    model = Ad
    extra = 0
    fields = ['title', 'img_url', 'link', 'clicks', 'views']
    readonly_fields = ['clicks', 'views']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    fields = [
        'title',
        'img_url',
        'link',
        'advertiser',
        'clicks',
        'views',
    ]

    readonly_fields = [
        'clicks',
        'views',
    ]

    list_display = [
        'id',
        'title',
        'link',
        'clicks',
        'views'
    ]



@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name',
        'total_clicks',
        'total_views'
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



