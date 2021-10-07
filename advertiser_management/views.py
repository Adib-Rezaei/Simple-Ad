from django.shortcuts import get_object_or_404, render
from django.template import response
from django.views.generic import ListView, RedirectView
from advertiser_management.forms import AdForm
from django.db.models import F
from advertiser_management.models import Ad
from advertiser_management.models import advertiser
from advertiser_management.models.advertiser import Advertiser


class AdRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        ad.clicks += 1
        ad.save()
        return ad.link


class AdvertisementView(ListView):
    template_name = 'ads.html'
    context_object_name = 'advertisers'
    queryset = Advertiser.objects.all()

    def get(self, request, *args, **kwargs):
        advertisers = self.get_queryset()
        self.object_list = advertisers
        context = self.get_context_data()

        Ad.objects.filter(advertiser__in=advertisers).update(views=F('views')+1)
        return self.render_to_response(context)


def AdCreateView(request):
    form = AdForm()

    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            print("HI")
            form.save()
    context = {'form': form}

    return render(request, 'ad_form.html', context)
