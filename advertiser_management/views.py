from django.core.exceptions import BadRequest
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, RedirectView
from django.views.generic.base import TemplateView

from advertiser_management.annotations import annotate_ads_report
from advertiser_management.forms import AdForm
from advertiser_management.models import Ad
from advertiser_management.models.advertiser import Advertiser
from advertiser_management.models.event import Click, View
from django import views

class AdRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        Click.objects.create(ad=ad, ip=kwargs['ip'])
        return ad.link


class AdvertisementView(ListView):
    template_name = 'ads.html'
    context_object_name = 'advertisers'
    queryset = Advertiser.objects.all()

    def get(self, request, *args, **kwargs):
        advertisers = self.get_queryset()
        self.object_list = advertisers

        for advertiser in advertisers:
            for ad in advertiser.ads.all():
                View.objects.create(ad=ad, ip=kwargs['ip'])

        return self.render_to_response(self.get_context_data())


class AdCreateView(TemplateView):
    template_name = 'ad_form.html'

    def get(self, request, *args, **kwargs):
        form = AdForm()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ads')



class AdReportView(views.View):
    queryset = Ad.objects.all()

    def get(self, request, hour):
        query = annotate_ads_report(self.queryset, int(hour))
        fields = ['id','title', 'advertiser__name', 'average_delay', 'total_rate', 'total_hour_events']
        return JsonResponse(data=list(query.values(*fields)), safe=False)
