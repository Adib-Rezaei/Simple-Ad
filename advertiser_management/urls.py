from django.urls import path

from advertiser_management.views import AdCreateView, AdRedirectView, AdReportView, AdvertisementView

urlpatterns = [
    path('ads/', AdvertisementView.as_view(), name='ads'),
    path('click/<int:pk>/', AdRedirectView.as_view(), name='click'),
    path('create_ad', AdCreateView.as_view()),
    path('ad_report/<int:hour>', AdReportView.as_view()),
]