
from django.contrib import admin
from advertiser_management.models.ad import Ad

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