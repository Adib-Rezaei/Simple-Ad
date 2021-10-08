class RetrieveIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        ip_dependant_views = ['AdvertisementView', 'AdRedirectView']
        if view_func.__name__ in ip_dependant_views:
            view_kwargs['ip'] = request.META.get('REMOTE_ADDR')