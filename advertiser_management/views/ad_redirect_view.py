from django.views.generic.base import RedirectView
from advertiser_management.models.ad import Ad
from advertiser_management.models.event import Click
from rest_framework.generics import get_object_or_404


class AdRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        Click.objects.create(ad=ad, ip=kwargs['ip'])
        return ad.link