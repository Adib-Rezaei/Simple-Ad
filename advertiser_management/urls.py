from django.urls import path
from advertiser_management.views.ad_redirect_view import AdRedirectView
from advertiser_management.views.ad_report_view import AdReportView
from advertiser_management.views.ad_views import  AdViewSet, AdvertiserViewSet
from rest_framework.routers import DefaultRouter

from advertiser_management.views.entry_views import AdvertiserEntryViewSet

router = DefaultRouter()
router.register('ad', AdViewSet, basename='ad')
router.register('advertiser', AdvertiserViewSet, basename='advertiser')
router.register('', AdvertiserEntryViewSet, basename='entry')

urlpatterns = [
    path('click/<int:pk>/', AdRedirectView.as_view(), name='click'),
    path('ad_report/<int:hour>', AdReportView.as_view()),
]

urlpatterns += router.urls