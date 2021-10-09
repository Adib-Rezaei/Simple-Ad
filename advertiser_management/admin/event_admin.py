
from django.contrib import admin
from advertiser_management.models.event import Click, View

class BaseEventAdmin(admin.ModelAdmin):

    list_display = ['id', 'ip', 'ad']

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